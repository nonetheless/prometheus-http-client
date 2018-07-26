import json
from prometheus.retrofit import Prometheus
from prometheus.exception import PrometheusGetFailException, PrometheusException
from prometheus.model.api_response import AlertManagersResult, Configs, ApiResponse


def get_api_result(rsp, is_obj=False, class_name=None):
    if rsp.status_code != 200:
        error = json.loads(rsp.text)
        return ApiResponse(status=rsp.status_code, data=rsp.text, errorType=error.get('errorTpye'),
                           error=error.get('error'))
    param = rsp.json()
    status = param.get('status')
    if status is None or status != 'success':
        # throw exception
        return ApiResponse(status=rsp.status_code, data=rsp.text, errorType="response status is failed",
                           error="response status is failed")
    if is_obj is False:
        return ApiResponse(status=rsp.status_code, data=param.get("data"))
    try:
        result_object = class_name(param.get('data'))
        return ApiResponse(status=rsp.status_code, data=result_object)
    except Exception as e:
        raise PrometheusException(e, status)


class PrometheusClient(object):

    def __init__(self, prometheus_url):
        self.prometheus = Prometheus(base_url=prometheus_url)

    def get_alertmanagers(self):
        rsp = self.prometheus.get_alertmanagers()
        return get_api_result(rsp, True, AlertManagersResult)

    def clean_tombstones(self):
        self.clean_tombstones()

    def configs(self):
        rsp = self.prometheus.configs()
        return get_api_result(rsp, True, Configs)

    def get_flags(self):
        rsp = self.prometheus.flags()
        return get_api_result(rsp)

    def label_value(self, value):
        rsp = self.prometheus.label_values(value)
        return get_api_result(rsp)

    def query(self, query, time):
        if time is None:
            rsp = self.prometheus.query(query)
        else:
            rsp = self.prometheus.query(query, time)
        return get_api_result(rsp)

    def query_range(self, query, start, end, step):
        rsp = self.prometheus.query_range(query, start, end, step)
        return get_api_result(rsp)
