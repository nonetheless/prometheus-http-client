from uplink import Consumer, get, post, headers, args, Path, Query


@headers({"Accept": "json"})
class Prometheus(Consumer):

    @get("api/v1/alertmanagers")
    def get_alertmanagers(self):
        """get alertmanagers"""
        pass

    @post("api/v1/admin/tsdb/clean_tombstones")
    def clean_tombstones(self):
        """clean_tombstones"""
        pass

    @get("api/v1/status/config")
    def configs(self):
        """get prometheus configs"""
        pass

    @get("api/v1/status/flags")
    def flags(self):
        """get flags"""
        pass

    @args(Path)
    @get("api/v1/label/{label}/values")
    def label_values(self, label):
        """label values"""
        pass

    @args(Query, Query)
    @get("api/v1/query")
    def query(self, query, time):
        """query api"""
        pass

    @args(Query)
    @get("api/v1/query")
    def query(self, query):
        """query api"""
        pass

    @args(Query, Query, Query, Query)
    @get("api/v1/query_range")
    def query_range(self, query, start, end, step):
        pass


