__all__ = ['PrometheusGetFailException','PrometheusException']


class BaseException(Exception):
    def __init__(self, message, status_code=None):
        super(BaseException, self).__init__(message)
        self.message = message
        self.status_code = status_code


class PrometheusGetFailException(BaseException):
    def __init__(self, message, status_code=None):
        super(PrometheusGetFailException, self).__init__(message, status_code)


class PrometheusException(BaseException):
    def __init__(self, message, status_code=None):
        super(PrometheusException, self).__init__(message, status_code)

