# Create a function that loads a file into memory then checks the database.
# Put this in a while loop
import sys
import time

from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, username='user', password='admin')
client.switch_database('canopus')


def mem_leak():
    total = 0
    array = []

    while True:
        try:
            with open('/Users/jayanand/PycharmProjects/canopus-technical-interview/memory_leak/file.txt') as f:
                lines = f.read()
                size = sys.getsizeof(lines)
            time.sleep(1)
            array.append(lines)
            total += size
            result = client.query(f"SELECT mem_used FROM os_poll GROUP BY * ORDER BY DESC LIMIT 1")
            points = result.get_points()
            for point in points:
                if point['mem_used'] >= 75:
                    sys.exit(1)
        except:
            print("An error occured")



if __name__ == "__main__":
    mem_leak()

