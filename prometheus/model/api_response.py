__all__ = ['ApiResponse', 'AlertManagersResult', 'AlertManager', 'Configs']

class ApiResponse(object):
    def __init__(self, status, data, errorType=None, error=None):
        self.status = status
        self.data = data
        self.errorType = errorType
        self.error = error

    def get_response_map(self, func):
        return {
            "status": self.status,
            "errorType": self.errorType,
            "error": self.error,
            "data": func(self.data)
        }


class AlertManager(object):
    def __init__(self, params=dict()):
        self.url = params.get('url')

    def __repr__(self):
        return "AlertManager{ url= " + self.url + "}"


class AlertManagersResult(object):
    """
    :param
    active_alert_managers: list(AlertManager)
    dropped_alert_managers: list(AlertManager)
    """

    def __init__(self, param=dict()):
        self.active_alert_managers = [AlertManager(i) for i in param.get("active_alert_managers", list())]
        self.dropped_alert_managers = [AlertManager(i) for i in param.get("dropped_alert_managers", list())]

class Configs(object):
    """
    :param
    yaml : string
    """

    def __init__(self, param=dict()):
        self.yaml = param.get('yaml')

