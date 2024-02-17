from rest_framework.serializers import ModelSerializer
from app.models import FileModel


class FileUploadSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        exclude = ['processed', 'uploaded_at']


class FileListSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['id', 'file', 'processed', 'uploaded_at']
