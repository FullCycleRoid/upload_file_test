from __future__ import absolute_import, unicode_literals

from celery import shared_task
from core.settings import supported_extensions

from .handlers import compress_video, resize_image, text_analysis
from .models import FileModel


@shared_task
def process_file(file_id):

    record = FileModel.objects.get(pk=file_id)
    ext = str(record.file).split('.')[-1]

    if ext in supported_extensions['video']:
        compress_video(record.file)

    if ext in supported_extensions['image']:
        resize_image(record.file)

    if ext in supported_extensions['text']:
        text_analysis(record.file)

    record.processed = True
    record.save()
