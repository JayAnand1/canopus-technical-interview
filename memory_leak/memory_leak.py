# Create a function that loads a file into memory then checks the database.
# Put this in a while loop
import sys
import time
from influx_service.influx_service import InfluxService
from pathlib import Path


def mem_leak():
    total = 0
    array = []
    influx_service = InfluxService()
    memory_usage_threshold = 75
    stop = False
    p = Path(__file__).with_name('file.txt')
    while not stop:
        try:
            with p.open('r') as f:
                lines = f.read()
                size = sys.getsizeof(lines)
            time.sleep(1)
            array.append(lines)
            total += size
            points = influx_service.read_os_datapoints()
            for point in points:
                print(f"Memory Used: {point['mem_used']}%")
                if point['mem_used'] >= memory_usage_threshold:
                    stop = True
                    break
        except Exception as e:
            print("An error occured", e)


if __name__ == "__main__":
    mem_leak()
