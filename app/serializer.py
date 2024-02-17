from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app.models import FileModel


class FileUploadSerializer(ModelSerializer):

    class Meta:
        model = FileModel
        exclude = ['processed', 'uploaded_at']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        ext = data['file'].name.split('.')[-1]
        # if ext not in :
        #     raise serializers.ValidationError("finish must occur after start")
        return data

class FileListSerializer(ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['id', 'file', 'processed', 'uploaded_at']
