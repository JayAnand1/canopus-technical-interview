import psutil
from influxdb import InfluxDBClient
import sched, time

client = InfluxDBClient(host='localhost', port=8086, username='user', password='admin')
client.switch_database('canopus')


def poll_os():
    while True:
        try:
            cpu, mem_used = retrieve_os_stats()
            write_to_influx(cpu, mem_used)
            time.sleep(1)
        except:
            print("An error occured")


def retrieve_os_stats():
    cpu = psutil.cpu_percent()
    mem_used = psutil.virtual_memory().percent
    return cpu, mem_used


def write_to_influx(cpu, mem_used):
    data = [{
        "measurement": "os_poll",
        "fields": {
            "cpu": cpu,
            "mem_used": mem_used,
        },
    }]
    client.write_points(data)


if __name__ == '__main__':
    poll_os()
