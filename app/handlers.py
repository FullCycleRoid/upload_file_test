def compress_video(filepath):
    try:
        print(f'Video: {filepath} compressed')
        return

    # handle some compress video errors
    except Exception as e:
        raise Exception(e)


def resize_image(filepath):
    try:
        print(f'Image: {filepath} resized')
        return

    # handle some resize image errors
    except Exception as e:
        raise Exception(e)


def text_analysis(filepath):
    try:
        print(f'text: {filepath} analyzed')
        return

    # handle some text analysis errors
    except Exception as e:
        raise Exception(e)
