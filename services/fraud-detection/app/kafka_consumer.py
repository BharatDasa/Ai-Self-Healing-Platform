from kafka import KafkaConsumer, KafkaProducer

from predictor import predict_fraud

from mongodb_client import (
    save_fraud_event,
    save_prediction
)

from metrics import (
    kafka_events_total,
    fraud_predictions_total,
    fraud_detected_total,
    fraud_safe_total
)

import json
import time

# ======================================================
# 🔥 START FRAUD DETECTION SERVICE
# ======================================================

def start():

    print(
        "🚀 Fraud Detection Service Started...",
        flush=True
    )

    # ==================================================
    # RETRY KAFKA CONNECTION
    # ==================================================

    while True:

        try:

            consumer = KafkaConsumer(

                "transactions",

                bootstrap_servers=
                "kafka.messaging.svc.cluster.local:9092",

                value_deserializer=lambda m:
                json.loads(m.decode("utf-8")),

                auto_offset_reset="latest",

                enable_auto_commit=True,

                group_id="fraud-group"
            )

            producer = KafkaProducer(

                bootstrap_servers=
                "kafka.messaging.svc.cluster.local:9092",

                value_serializer=lambda v:
                json.dumps(v).encode("utf-8")
            )

            print(
                "✅ Connected to Kafka",
                flush=True
            )

            break

        except Exception as e:

            print(
                f"❌ Kafka not ready, retrying... {e}",
                flush=True
            )

            time.sleep(5)

    print(
        "\n👀 Listening for transactions...\n",
        flush=True
    )

    # ==================================================
    # PROCESS EVENTS
    # ==================================================

    for message in consumer:

        try:

            txn = message.value

            kafka_events_total.inc()

            # ==========================================
            # EVENT HEADER
            # ==========================================

            print(
                "\n"
                "=====================================================",
                flush=True
            )

            print(
                "📥 TRANSACTION RECEIVED",
                flush=True
            )

            print(
                f"👤 User      : {txn['user_id']}",
                flush=True
            )

            print(
                f"💰 Amount    : {txn['amount']}",
                flush=True
            )

            print(
                f"🌍 Location  : {txn['location']}",
                flush=True
            )

            print(
                f"🕒 Timestamp : {txn['timestamp']}",
                flush=True
            )

            print(
                "=====================================================",
                flush=True
            )

            # ==========================================
            # STORE RAW EVENT
            # ==========================================

            save_fraud_event(txn)

            # ==========================================
            # ML PREDICTION
            # ==========================================

            prediction = predict_fraud(txn)

            save_prediction(prediction)

            fraud_predictions_total.inc()

            # ==========================================
            # PREDICTION OUTPUT
            # ==========================================

            print(
                "\n🧠 ML INFERENCE RESULT",
                flush=True
            )

            print(
                f"🎯 Prediction  : "
                f"{prediction['fraud_prediction']}",
                flush=True
            )

            print(
                f"📊 Probability : "
                f"{prediction['fraud_probability']}",
                flush=True
            )

            print(
                f"⚠️ Risk Score  : "
                f"{prediction.get('risk_score', 0)}",
                flush=True
            )

            # ==========================================
            # FRAUD DETECTION LOGIC
            # ==========================================

            if prediction["fraud_prediction"] == 1:

                fraud_detected_total.inc()

                print(
                    "\n🚨 FRAUD DETECTED",
                    flush=True
                )

                print(
                    f"👤 User     : "
                    f"{prediction['user_id']}",
                    flush=True
                )

                print(
                    f"💰 Amount   : "
                    f"{prediction['amount']}",
                    flush=True
                )

                print(
                    f"📊 Risk     : "
                    f"{prediction['fraud_probability']}",
                    flush=True
                )

                # ======================================
                # SEND ALERT
                # ======================================

                producer.send(
                    "fraud_alerts",
                    prediction
                )

                producer.flush()

                print(
                    "\n📤 Alert sent to fraud_alerts",
                    flush=True
                )

            else:

                fraud_safe_total.inc()

                print(
                    "\n✅ SAFE TRANSACTION",
                    flush=True
                )

        except Exception as e:

            print(
                f"\n❌ Error processing message: {e}",
                flush=True
            )
