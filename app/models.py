from datetime import datetime
from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='store/files')
    uploaded_at = models.DateTimeField(default=datetime.now())
    processed = models.BooleanField(default=False)
