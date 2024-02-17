from time import sleep

from app.exception import AnalysisException, ResizeException, CompressException


def compress_video(filepath):
    try:
        sleep(5)
        print(f'Video: {filepath} compressed')

    except CompressException as e:
        raise CompressException(e)


def resize_image(filepath):
    try:
        sleep(5)
        print(f'Image: {filepath} resized')

    except ResizeException as e:
        raise ResizeException(e)


def text_analysis(filepath):
    try:
        sleep(5)
        print(f'text: {filepath} analyzed')

    except AnalysisException as e:
        raise AnalysisException(e)
