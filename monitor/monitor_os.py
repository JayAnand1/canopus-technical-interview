import psutil
import time
from influx_service.influx_service import InfluxService

def poll_os():
    influx_service = InfluxService()
    while True:
        try:
            time.sleep(1)
            cpu, mem_used = retrieve_os_stats()
            influx_service.add_os_datapoint(cpu, mem_used)
            print(f"Logged: CPU {cpu}%, MEM {mem_used}%")
        except:
            print("An error occured")


def retrieve_os_stats():
    cpu = psutil.cpu_percent()
    mem_used = psutil.virtual_memory().percent
    return cpu, mem_used


if __name__ == '__main__':
    poll_os()
