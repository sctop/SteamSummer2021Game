class LangStringError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class LangStringInitError(LangStringError):
    def __init__(self, message="初始化LangString时遇到错误"):
        super().__init__(message)


class LangStringLoadError(LangStringInitError):
    def __init__(self, message="载入LangString内容时遇到错误"):
        super().__init__(message)
