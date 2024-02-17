from __future__ import absolute_import, unicode_literals

from celery import shared_task

from core.settings import supported_extensions
from .models import FileModel
from core.celery import app 
import time


@app.task
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return "0"
    elif n == 2:
        return "0, 1"
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return ', '.join(map(str, fib_sequence))


@shared_task
def process_file(file_id):

    record = FileModel.objects.get(pk=file_id)
    ext = str(record.file).split('.')[-1]

    if ext in supported_extensions['video']:
        compress_video(record.file)

    elif ext in supported_extensions['image']:
        resize_image(record.file)

    elif ext in supported_extensions['text']:
        text_analysis(record.file)

    else:
        raise Exception("File type not supported. Process Failed")

    record.processed = True
    record.save()


def compress_video(filename):
    try:
        print(f'Video: {filename} compressed')
        return

    # handle some compress errors
    except Exception as e:
        raise Exception(e)


def resize_image(filename):
    try:
        print(f'Image: {filename} resized')
        return

    # handle some resize errors
    except Exception as e:
        raise Exception(e)


def text_analysis(filename):
    try:
        print(f'text: {filename} analyzed')
        return

    # handle some analysis errors
    except Exception as e:
        raise Exception(e)
