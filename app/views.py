from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.serializer import FileListSerializer, FileUploadSerializer
from app.tasks import *


class ListView(APIView):

    def get(self, request):
        objects = FileModel.objects.all()
        serializer = FileListSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadView(APIView):
    serializer_class = FileUploadSerializer

    def post(self, request):

        file = request.FILES.get('file', None)
        instance = FileModel(processed=False, uploaded_at=datetime.now(), file=file)
        instance.save()

        # Call the Celery task
        process_file.delay(file_id=instance.id)

        return Response(
            data={
                'id':  instance.id,
                'uploaded_at': instance.uploaded_at,
                'processed': instance.processed,
            },
            status=status.HTTP_201_CREATED
        )
