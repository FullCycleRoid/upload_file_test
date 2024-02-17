from app.exception import AnalysisException, ResizeException, CompressException


def compress_video(filepath):
    try:
        print(f'Video: {filepath} compressed')
        return

    # handle some compress video errors
    except CompressException as e:
        raise CompressException(e)


def resize_image(filepath):
    try:
        print(f'Image: {filepath} resized')
        return

    # handle some resize image errors
    except ResizeException as e:
        raise ResizeException(e)


def text_analysis(filepath):
    try:
        print(f'text: {filepath} analyzed')
        return

    # handle some text analysis errors
    except AnalysisException as e:
        raise AnalysisException(e)
