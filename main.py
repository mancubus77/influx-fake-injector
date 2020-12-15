import json
import random
from influxdb import InfluxDBClient
from datetime import datetime
from kafka import KafkaProducer

TOPIC = "telemetry"
BOOTSTRAP_SERVERS = ["my-cluster-kafka-brokers:9092"]
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)
metric = {
    "measurement": "",
    "tags": {},
    "fields": {},
}
# client = InfluxDBClient("127.0.0.1", 8480, path="/insert/0/influx/")


def run():
    while True:
        for i in range(1, 10):
            metric["measurement"] = "interface"
            metric["tags"] = {
                "TID": f"22RR-HEF-01-0{i}",
                "name": f"GigabitEthernet0/0/{i}",
            }
            metric["fields"] = {
                "bytes_in": random.randint(0, 100),
                "bytes": random.randint(0, 100),
            }
            metric["ts"] = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
            print(json.dumps(metric))
            # client.write_points([metric])
            producer.send(TOPIC, bytes(json.dumps(metric)))


if __name__ == "__main__":
    run()
