from app.exception import AnalysisException, ResizeException, CompressException


def compress_video(filepath):
    try:
        print(f'Video: {filepath} compressed')

    except CompressException as e:
        raise CompressException(e)


def resize_image(filepath):
    try:
        print(f'Image: {filepath} resized')

    except ResizeException as e:
        raise ResizeException(e)


def text_analysis(filepath):
    try:
        print(f'text: {filepath} analyzed')

    except AnalysisException as e:
        raise AnalysisException(e)
