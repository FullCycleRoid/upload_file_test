import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from parameterized import parameterized
from rest_framework import status
from unittest.mock import patch

from app.exception import ExtensionException
from app.models import FileModel
from app.tasks import process_file


class UploadFileTestCase(TestCase):

    @parameterized.expand([
        ('mp4', 'video/mp4'),
        ('mov', 'video/quicktime'),
        ('txt', 'text/plain'),
        ('doc', 'application/msword'),
        ('jpg', 'image/jpg'),
        ('jpeg', 'image/jpeg'),
        ('png', 'image/png')
    ])
    # monkey patch for connecting celery to database
    @patch('app.tasks.process_file.delay', new=process_file)
    def test_upload_file_valid_extensions_201(self, ext, mime_type):
        filename = f"test_file.{ext}"
        tmp_file = SimpleUploadedFile(filename, b"file_content", content_type=mime_type)

        response = self.client.post('/api/upload/', {'file': tmp_file}, format='multipart')
        response_json = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_json['processed'], False)

        record = FileModel.objects.get(pk=response_json['id'])

        self.assertEqual(record.id, response_json['id'])
        self.assertEqual(record.processed, True)

        os.remove(str(record.file))

    @patch('app.tasks.process_file.delay', new=process_file)
    def test_process_file_failed(self):
        filename = f"test_file123.zip"
        tmp_file = SimpleUploadedFile(filename, b"file_content", content_type='application/zip')

        self.assertRaises(
            ExtensionException,
            self.client.post,
            "/api/upload/",
            {'file': tmp_file},
            format='multipart'
        )

        os.remove(f'store/files/{tmp_file.name}')

    @patch('app.tasks.process_file.delay', new=process_file)
    def test_files_list_200(self):
        for fn in range(10):
            tmp_file = SimpleUploadedFile(f'{fn}.png', b"file_content")
            self.client.post('/api/upload/', {'file': tmp_file}, format='multipart')

        rows_count = FileModel.objects.all()
        self.assertEqual(len(rows_count), 10)

        for _ in rows_count:
            os.remove(str(_.file))
