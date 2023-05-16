# Create a function that loads a file into memory then checks the database.
# Put this in a while loop
import sys

from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, username='user', password='admin')
client.switch_database('canopus')


def mem_leak():
    array = []
    with open('/Users/jayanand/PycharmProjects/canopus-technical-interview/file.txt') as f:
        lines = f.read().splitlines()
    while True:
        time.sleep(1)
        array.append(lines)
        result = client.query(f"SELECT mem_used FROM os_poll GROUP BY * ORDER BY DESC LIMIT 1")
        points = result.get_points()
        for point in points:
            if point['mem_used'] >= 80:
                sys.exit(1)



if __name__ == "__main__":
    mem_leak()

