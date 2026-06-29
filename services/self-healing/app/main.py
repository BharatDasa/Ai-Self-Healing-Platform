from kafka_consumer import start

from predict_scale import predict_action

from actions import restart

from metrics import (
    ai_event_rate,
    ai_model_score,
    ai_target_replicas,
    scaling_actions_total,
    restart_actions_total,
    start_metrics_server
)

from postgres_client import (
    save_scaling_event,
    save_restart_event
)

import time


# ======================================================
# PLATFORM INFO
# ======================================================

SERVICE_NAME = "self-healing-engine"

VERSION = "10.0-ai-keda-autoscaling"

ENVIRONMENT = "production"


# ======================================================
# CONFIGURATION
# ======================================================

WINDOW_SECONDS = 60

COOLDOWN_SECONDS = 60

MIN_AMOUNT = 8000

RESTART_LOAD = 50

MAX_REPLICAS = 5

MIN_REPLICAS = 1

TARGET_ROLLOUT = "fraud-detection"

TARGET_NAMESPACE = "ai-platform"


# ======================================================
# RUNTIME STATE
# ======================================================

event_buffer = []

last_action_time = 0


# ======================================================
# CLEAN OLD EVENTS
# ======================================================

def cleanup_old_events(now):

    global event_buffer

    event_buffer = [

        e for e in event_buffer

        if now - e["ts"] < WINDOW_SECONDS
    ]


# ======================================================
# PROCESS EVENT
# ======================================================

def process(event):

    global event_buffer
    global last_action_time

    now = time.time()

    print(
        f"\n📥 EVENT RECEIVED: {event}",
        flush=True
    )

    try:

        # ==================================================
        # VALIDATE EVENT
        # ==================================================

        amount = float(
            event.get("amount", 0)
        )

        # ==================================================
        # FILTER LOW SIGNAL
        # ==================================================

        if amount < MIN_AMOUNT:

            print(
                "🟡 Ignored low-risk transaction",
                flush=True
            )

            return

        # ==================================================
        # CLEANUP WINDOW
        # ==================================================

        cleanup_old_events(now)

        # ==================================================
        # APPEND EVENT
        # ==================================================

        event["ts"] = now

        event_buffer.append(event)

        current_load = len(event_buffer)

        # ==================================================
        # EVENT LOGGING
        # ==================================================

        print(
            f"📊 Active anomaly events: "
            f"{current_load}",
            flush=True
        )

        print(
            f"📦 Sliding window amounts: "
            f"{[e.get('amount', 0) for e in event_buffer]}",
            flush=True
        )

        # ==================================================
        # UPDATE METRICS
        # ==================================================

        ai_event_rate.set(current_load)

        # ==================================================
        # COOLDOWN PROTECTION
        # ==================================================

        cooldown_remaining = (
            COOLDOWN_SECONDS -
            (now - last_action_time)
        )

        if cooldown_remaining > 0:

            print(
                f"⏳ Cooldown active "
                f"({round(cooldown_remaining)}s remaining)",
                flush=True
            )

            return

        # ==================================================
        # ML PREDICTION
        # ==================================================

        decision, replicas, score, event_rate = (
            predict_action(event_buffer)
        )

        decision = str(
            decision
        ).strip().upper()

        # ==================================================
        # SAFETY LIMITS
        # ==================================================

        replicas = max(
            MIN_REPLICAS,
            replicas
        )

        replicas = min(
            MAX_REPLICAS,
            replicas
        )

        # ==================================================
        # UPDATE AI METRICS
        # ==================================================

        ai_model_score.set(score)

        ai_target_replicas.set(replicas)

        # ==================================================
        # STORE IMPORTANT EVENTS
        # ==================================================

        if decision != "NORMAL":

            save_scaling_event(

                TARGET_ROLLOUT,

                decision,

                replicas,

                score,

                event_rate
            )

        # ==================================================
        # EXTREME ANOMALY OVERRIDE
        # ==================================================

        if current_load >= RESTART_LOAD:

            print(
                "🔥 Extreme anomaly threshold reached "
                "→ forcing rollout restart",
                flush=True
            )

            decision = "RESTART"

        # ==================================================
        # FINAL DECISION
        # ==================================================

        print(
            f"🤖 FINAL AI DECISION → {decision}",
            flush=True
        )

        # ==================================================
        # SCALE SIGNAL
        # ==================================================

        if decision == "SCALE":

            scaling_actions_total.inc()

            print(
                "⚡ High load detected "
                "→ AI metric published to Prometheus",
                flush=True
            )

            print(
                f"📈 Recommended replicas: {replicas}",
                flush=True
            )

            print(
                "📡 KEDA consuming AI scaling metric",
                flush=True
            )

            print(
                "🛰️ Argo Rollouts scaling workload",
                flush=True
            )

        # ==================================================
        # ELEVATED STATE
        # ==================================================

        elif decision == "ELEVATED":

            print(
                "🟠 Elevated anomaly pressure detected",
                flush=True
            )

            print(
                "📈 Warm scaling recommendation published",
                flush=True
            )

            print(
                f"⚡ Suggested replicas: "
                f"{replicas}",
                flush=True
            )

            print(
                "🛰️ KEDA remains active",
                flush=True
            )

        # ==================================================
        # RESTART SIGNAL
        # ==================================================

        elif decision == "RESTART":

            restart_actions_total.inc()

            print(
                "🔄 Triggering rollout restart",
                flush=True
            )

            # ==============================================
            # RESET REPLICA SIGNAL
            # ==============================================

            ai_target_replicas.set(1)

            # ==============================================
            # STORE RESTART EVENT
            # ==============================================

            save_restart_event(

                TARGET_ROLLOUT,

                "extreme anomaly detected",

                score
            )

            # ==============================================
            # EXECUTE RESTART
            # ==============================================

            restart(

                TARGET_ROLLOUT,

                TARGET_NAMESPACE
            )

            last_action_time = now

            return

        # ==================================================
        # STABLE
        # ==================================================

        else:

            ai_target_replicas.set(1)

            print(
                "🟢 System stable — no action required",
                flush=True
            )

            print(
                "📉 AI scaling recommendation reset to 1",
                flush=True
            )

    except Exception as e:

        print(
            f"❌ Self-healing engine failure: {e}",
            flush=True
        )


# ======================================================
# MAIN
# ======================================================

def main():

    print(
        "\n"
        "=====================================================\n"
        "🤖 AI SELF-HEALING ENGINE STARTED\n"
        "=====================================================\n"
        f"📦 Service      : {SERVICE_NAME}\n"
        f"🧠 Version      : {VERSION}\n"
        f"🌍 Environment  : {ENVIRONMENT}\n"
        f"🐘 Database     : PostgreSQL\n"
        f"📡 Streaming    : Kafka\n"
        f"📊 Metrics      : Prometheus\n"
        f"☸️ Runtime      : Kubernetes\n"
        f"🛰️ Progressive  : Argo Rollouts\n"
        f"⚡ Autoscaling  : KEDA\n"
        f"🧠 AI Engine    : Predictive autonomous scaling\n"
        "=====================================================\n",
        flush=True
    )

    # ==================================================
    # START METRICS SERVER
    # ==================================================

    start_metrics_server()

    # ==================================================
    # START KAFKA CONSUMER
    # ==================================================

    start(process)


# ======================================================
# ENTRYPOINT
# ======================================================

if __name__ == "__main__":

    main()
