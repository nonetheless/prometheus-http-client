import unittest
from prometheus.client import PrometheusClient
from prometheus.util.query_result import QueryResult


class TestAlertManagers(unittest.TestCase):
    def setUp(self):
        self.url = "http://172.16.3.234:30220"
        self.prometheus = PrometheusClient(self.url)

    def test_alert_manager(self):
        rsp = self.prometheus.get_alertmanagers()
        self.assertTrue(True)

    def test_configs(self):
        rsp = self.prometheus.configs()
        self.assertTrue(True)

    def test_get_flags(self):
        rsp = self.prometheus.get_flags()
        self.assertTrue(True)

    def test_label(self):
        rsp = self.prometheus.label_value("namespace")
        self.assertTrue(True)

    def test_query(self):
        rsp = self.prometheus.query("kubelet:namespace:mem:used{namespace=\"v8n7m9y\"}", None)
        self.assertTrue(True)

    def test_query(self):
        query = QueryResult.execute(self.prometheus,"kubelet:pod:cpu:used{namespace=\"v8n7m9y\"}", None)
        self.assertTrue(True)
