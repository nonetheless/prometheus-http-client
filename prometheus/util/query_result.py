from prometheus.model.query_model import Sample, SampleStream, Scalar, PString
from prometheus.exception import PrometheusException


class QueryResult(object):
    def __init__(self, json):
        self.json = json

    def get_type(self):
        typenode = self.json.get("resultType")
        return typenode

    def as_matrix(self):
        return [SampleStream(i) for i in self.json]

    def as_vector(self):
        return [Sample(i) for i in self.json]

    def as_scalar(self):
        return Scalar(self.json)

    def as_pstring(self):
        return PString(self.json)

    def as_dict(self, keyword):
        rsp = dict()
        [rsp.update(self._get_dict(i, keyword)) for i in self.json]
        return rsp

    def _get_dict(self, params, keyword):
        metric = params.get('metric')
        dict_key = metric.get(keyword)
        value = params.get('value')
        return {str(dict_key): value}

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
