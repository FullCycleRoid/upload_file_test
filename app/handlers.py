from app.exception import AnalysisException, ResizeException, CompressException


def compress_video(filepath):
    try:
        print(f'Video: {filepath} compressed')
        return

    except CompressException as e:
        raise CompressException(e)


def resize_image(filepath):
    try:
        print(f'Image: {filepath} resized')
        return

    except ResizeException as e:
        raise ResizeException(e)


def text_analysis(filepath):
    try:
        print(f'text: {filepath} analyzed')
        return

    except AnalysisException as e:
        raise AnalysisException(e)
