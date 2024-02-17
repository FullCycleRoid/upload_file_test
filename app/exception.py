class ExtensionException(Exception):
    pass


class ResizeException(TypeError, ValueError, Exception):
    pass


class CompressException(TypeError, ValueError, Exception):
    pass


class AnalysisException(TypeError, ValueError, Exception):
    pass
