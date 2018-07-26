class SampleStream(object):
    """
    :param
    metric: map
    value: list
    """

    def __init__(self, params=dict()):
        self.metric = params.get('metric')
        self.value = params.get('value')


class Sample(object):
    """
    :param
    metric: map
    value: long
    timestamp: long
    """

    def __init__(self, params=dict()):
        self.metric = params.get('metric')
        self.value = params.get('value')
        self.timestamp = params.get('timestamp')


class Scalar(object):
    """
    :param
    value: long
    timestramp: long
    """

    def __init__(self, params=dict()):
        self.value = params.get('value')
        self.timestamp = params.get('timestamp')


class PString(object):
    """
    :param
    value: long
    timestramp: long
    """

    def __init__(self, params=dict()):
        self.value = params.get('value')
        self.timestamp = params.get('timestamp')
