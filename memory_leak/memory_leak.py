# Create a function that loads a file into memory then checks the database.
# Put this in a while loop
import sys
import time
from influx_service.influx_service import InfluxService


def mem_leak():
    total = 0
    array = []
    influx_service = InfluxService()
    memory_usage_threshold = 75
    stop = False
    while not stop:
        try:
            with open('/Users/jayanand/PycharmProjects/canopus-technical-interview/memory_leak/file.txt') as f:
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
        except:
            print("An error occured")


if __name__ == "__main__":
    mem_leak()
