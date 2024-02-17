def compress_video(filename):
    try:
        print(f'Video: {filename} compressed')
        return

    # handle some compress video errors
    except Exception as e:
        raise Exception(e)


def resize_image(filename):
    try:
        print(f'Image: {filename} resized')
        return

    # handle some resize image errors
    except Exception as e:
        raise Exception(e)


def text_analysis(filename):
    try:
        print(f'text: {filename} analyzed')
        return

    # handle some text analysis errors
    except Exception as e:
        raise Exception(e)
