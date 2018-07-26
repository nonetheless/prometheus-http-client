from prometheus.model.query_model import Sample, SampleStream, Scalar, PString
from prometheus.exception import PrometheusException


class QueryResult(object):
    def __init__(self, json):
        self.json = json

    def get_type(self):
        typenode = self.json.get("resultType")
        return typenode

    def asMatrix(self):
        return [SampleStream(i) for i in self.json]

    def asVector(self):
        return [Sample(i) for i in self.json]

    def asScalar(self):
        return Scalar(self.json)

    def asPString(self):
        return PString(self.json)

    @classmethod
    def execute(cls, prometheus, query, ts):
        api_response = prometheus.query(query, ts)
        if api_response.status != 200:
            raise PrometheusException(
                message="{errorType:%s;error:%s}".format(api_response.errorType, api_response.error),
                status_code=api_response.status)
        return QueryResult(api_response.data.get("result"))

    @classmethod
    def execute_range(cls, prometheus, query, start, end, step):
        api_response = prometheus.query_range(query, start, end, step)
        if api_response.status != 200:
            raise PrometheusException(
                message="{errorType:%s;error:%s}".format(api_response.errorType, api_response.error),
                status_code=api_response.status)
        return QueryResult(api_response.data.get("result"))
