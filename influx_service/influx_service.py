from influxdb import InfluxDBClient
import sys


class InfluxService:
    def __init__(self):
        self.client = InfluxDBClient(host='localhost', port=8086, username='user', password='admin')
        self.client.switch_database('canopus')

    def add_os_datapoint(self, cpu, mem_used):
        data = [{
            "measurement": "os_poll",
            "fields": {
                "cpu": cpu,
                "mem_used": mem_used,
            },
        }]
        self.client.write_points(data)

    def read_os_datapoints(self):
        result = self.client.query(f"SELECT * FROM os_poll GROUP BY * ORDER BY DESC LIMIT 1")
        points = result.get_points()
        return points
