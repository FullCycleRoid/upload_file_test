import base64
from datetime import datetime

from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import FileModel
from app.serializer import FileListSerializer, FileUploadSerializer
# from .tasks import my_celery_task

from app.tasks import *
import time


class ListView(APIView):

    def get(self, request):
        objects = FileModel.objects.all()
        serializer = FileListSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UploadView(APIView):
    serializer_class = FileUploadSerializer

    def post(self, request):
        instance = FileModel(processed=False, uploaded_at=datetime.now(), file=request.FILES['file'])
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
