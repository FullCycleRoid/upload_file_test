from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app.models import FileModel
from core.settings import supported_extensions


class FileUploadSerializer(ModelSerializer):

    class Meta:
        model = FileModel
        # exclude fields from swagger
        exclude = ['processed', 'uploaded_at']

    def validate_file(self, value):
        """
        Upload valid extension file only
        """
        file_ext = value.name.split('.')[-1]

        all_extensions = supported_extensions['video'] + supported_extensions['text'] + supported_extensions['image']
        if file_ext not in all_extensions:
            raise serializers.ValidationError("File type not supported. Uploaded Failed")

        return value


class FileListSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['id', 'file', 'processed', 'uploaded_at']
