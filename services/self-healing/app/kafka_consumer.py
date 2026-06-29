from kafka import KafkaConsumer

import json
import time

from metrics import (
    kafka_alerts_total,
    kafka_errors_total
)


# ======================================================
# KAFKA CONFIG
# ======================================================

BOOTSTRAP_SERVERS = (
    "kafka.messaging.svc.cluster.local:9092"
)

TOPIC = "fraud_alerts"

# ======================================================
# PRODUCTION CONSUMER GROUP
# ======================================================

GROUP_ID = "self-healing-production"

CLIENT_ID = "self-healing-service"


# ======================================================
# CREATE CONSUMER
# ======================================================

def create_consumer():

    return KafkaConsumer(

        TOPIC,

        bootstrap_servers=BOOTSTRAP_SERVERS,

        value_deserializer=lambda m:
        json.loads(m.decode("utf-8")),

        # ==================================================
        # OFFSET STRATEGY
        # ==================================================

        auto_offset_reset="latest",

        enable_auto_commit=True,

        group_id=GROUP_ID,

        client_id=CLIENT_ID,

        # ==================================================
        # CONNECTION STABILITY
        # ==================================================

        consumer_timeout_ms=1000,

        session_timeout_ms=30000,

        heartbeat_interval_ms=10000,

        request_timeout_ms=40000,

        api_version_auto_timeout_ms=30000,

        max_poll_interval_ms=300000,

        # ==================================================
        # CONTROLLED MESSAGE BATCHING
        # ==================================================

        max_poll_records=5
    )


# ======================================================
# START CONSUMER
# ======================================================

def start(callback):

    print(
        "🚀 Connecting to Kafka (fraud_alerts)...",
        flush=True
    )

    # ==================================================
    # CONNECTION LOOP
    # ==================================================

    while True:

        consumer = None

        try:

            # ==============================================
            # CREATE CONSUMER
            # ==============================================

            consumer = create_consumer()

            print(
                f"✅ Connected to Kafka @ "
                f"{BOOTSTRAP_SERVERS}",
                flush=True
            )

            print(
                "👀 Waiting for fraud alerts...\n",
                flush=True
            )

            # ==============================================
            # MESSAGE LOOP
            # ==============================================

            while True:

                try:

                    records = consumer.poll(
                        timeout_ms=5000
                    )

                    # ======================================
                    # NO EVENTS
                    # ======================================

                    if not records:

                        continue

                    for _, messages in records.items():

                        for msg in messages:

                            data = msg.value

                            kafka_alerts_total.inc()

                            print(
                                f"⚠️ ALERT RECEIVED: "
                                f"{data}",
                                flush=True
                            )

                            # ==============================
                            # SEND TO AI ENGINE
                            # ==============================

                            callback(data)

                except Exception as e:

                    kafka_errors_total.inc()

                    print(
                        f"❌ Message processing error: "
                        f"{e}",
                        flush=True
                    )

                    time.sleep(2)

        except Exception as e:

            kafka_errors_total.inc()

            print(
                f"❌ Kafka connection failed: {e}",
                flush=True
            )

            print(
                "🔁 Retrying in 5 seconds...\n",
                flush=True
            )

            time.sleep(5)

        finally:

            # ==============================================
            # CLEAN SHUTDOWN
            # ==============================================

            try:

                if consumer:

                    consumer.close()

                    print(
                        "🔌 Kafka consumer closed",
                        flush=True
                    )

            except Exception as e:

                print(
                    f"⚠️ Consumer cleanup failed: {e}",
                    flush=True
                )
