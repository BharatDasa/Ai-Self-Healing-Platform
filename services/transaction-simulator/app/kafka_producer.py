from kafka import KafkaProducer
import json
import time
from generator import generate_transaction


def start():
    print("🔥 Simulator Booting...", flush=True)

    # 🔁 Retry loop (Kafka may not be ready when pod starts)
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka.messaging.svc.cluster.local:9092',
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                acks="all",                     # ✅ ensure delivery
                retries=5,                     # ✅ retry on failure
                linger_ms=10
            )

            print("✅ Kafka Connected", flush=True)
            break

        except Exception as e:
            print(f"❌ Kafka not ready, retrying... {e}", flush=True)
            time.sleep(5)

    # 🔄 Continuous event stream
    while True:
        try:
            txn = generate_transaction()
            print("📤 Sending:", txn, flush=True)

            future = producer.send("transactions", txn)

            # ✅ IMPORTANT: confirm message actually sent
            record_metadata = future.get(timeout=10)

            print(
                f"✅ Delivered to topic={record_metadata.topic} "
                f"partition={record_metadata.partition} "
                f"offset={record_metadata.offset}",
                flush=True
            )

        except Exception as e:
            print(f"❌ Send failed: {e}", flush=True)

        time.sleep(2)
