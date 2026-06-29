import pandas as pd

from scaling_model import model

from metrics import (
    ai_event_rate,
    ai_model_score,
    ai_target_replicas
)

# ======================================================
# CONFIG
# ======================================================

MIN_REPLICAS = 1

MAX_REPLICAS = 5

# Sustained traffic thresholds
LOW_PRESSURE_EVENTS = 5
MEDIUM_PRESSURE_EVENTS = 10
HIGH_PRESSURE_EVENTS = 15

# Fraud intensity thresholds
MEDIUM_RISK_SCORE = 0.85
HIGH_RISK_SCORE = 0.95


# ======================================================
# BUILD FEATURES
# ======================================================

def build_features(events):

    if not events:

        return {

            "event_rate": 0,

            "model_score": 0.0,

            "avg_amount": 0.0,

            "max_amount": 0.0
        }

    # ==================================================
    # EVENT RATE
    # ==================================================

    event_rate = len(events)

    # ==================================================
    # SAFE AMOUNT EXTRACTION
    # ==================================================

    amounts = []

    for e in events:

        try:

            amounts.append(

                float(
                    e.get("amount", 0)
                )
            )

        except Exception:

            continue

    # ==================================================
    # SAFETY
    # ==================================================

    if not amounts:

        avg_amount = 0.0

        max_amount = 0.0

    else:

        avg_amount = (
            sum(amounts) / len(amounts)
        )

        max_amount = max(amounts)

    # ==================================================
    # NORMALIZED SCORE
    # ==================================================

    model_score = round(
        avg_amount / 10000,
        5
    )

    return {

        "event_rate": event_rate,

        "model_score": model_score,

        "avg_amount": avg_amount,

        "max_amount": max_amount
    }


# ======================================================
# PREDICT ACTION
# ======================================================

def predict_action(events):

    try:

        # ==================================================
        # FEATURE ENGINEERING
        # ==================================================

        features = build_features(events)

        event_rate = features["event_rate"]

        model_score = features["model_score"]

        avg_amount = features["avg_amount"]

        max_amount = features["max_amount"]

        # ==================================================
        # LOGGING
        # ==================================================

        print(
            "\n"
            "-----------------------------------------------------",
            flush=True
        )

        print(
            f"🧪 Event Rate      : {event_rate}",
            flush=True
        )

        print(
            f"💰 Avg Amount      : "
            f"{round(avg_amount, 2)}",
            flush=True
        )

        print(
            f"🔥 Max Amount      : "
            f"{round(max_amount, 2)}",
            flush=True
        )

        print(
            f"🧠 Model Score     : "
            f"{model_score}",
            flush=True
        )

        # ==================================================
        # BUILD ML DATAFRAME
        # ==================================================

        df = pd.DataFrame([{

            "event_rate":
            event_rate,

            "model_score":
            model_score

        }])

        # ==================================================
        # ML PREDICTION
        # ==================================================

        raw_prediction = model.predict(df)[0]

        replicas = int(raw_prediction)

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
        # PRESSURE SCORE
        # ==================================================

        pressure_score = 0

        # --------------------------------------------------
        # EVENT PRESSURE
        # --------------------------------------------------

        if event_rate >= HIGH_PRESSURE_EVENTS:

            pressure_score += 3

        elif event_rate >= MEDIUM_PRESSURE_EVENTS:

            pressure_score += 2

        elif event_rate >= LOW_PRESSURE_EVENTS:

            pressure_score += 1

        # --------------------------------------------------
        # RISK PRESSURE
        # --------------------------------------------------

        if model_score >= HIGH_RISK_SCORE:

            pressure_score += 2

        elif model_score >= MEDIUM_RISK_SCORE:

            pressure_score += 1

        # ==================================================
        # FINAL DECISION
        # ==================================================

        if pressure_score >= 4:

            action = "SCALE"

        elif pressure_score >= 2:

            action = "ELEVATED"

        else:

            action = "NORMAL"

        # ==================================================
        # REPLICA NORMALIZATION
        # ==================================================

        if action == "NORMAL":

            replicas = 1

        elif action == "ELEVATED":

            replicas = 2

        elif action == "SCALE":

            if event_rate >= 30:

                replicas = 5

            elif event_rate >= 20:

                replicas = 4

            else:

                replicas = 3

        # ==================================================
        # FINAL SAFETY LIMITS
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
        # UPDATE METRICS
        # ==================================================

        ai_event_rate.set(event_rate)

        ai_model_score.set(model_score)

        ai_target_replicas.set(replicas)

        # ==================================================
        # FINAL LOGGING
        # ==================================================

        print(
            f"📊 Pressure Score  : "
            f"{pressure_score}",
            flush=True
        )

        print(
            f"🤖 ML Decision     : "
            f"{action}",
            flush=True
        )

        print(
            f"📈 Suggested Scale : "
            f"{replicas}",
            flush=True
        )

        print(
            "-----------------------------------------------------\n",
            flush=True
        )

        # ==================================================
        # RETURN
        # ==================================================

        return (

            action,

            replicas,

            model_score,

            event_rate
        )

    except Exception as e:

        print(
            f"❌ Scaling prediction failed: {e}",
            flush=True
        )

        return (

            "NORMAL",

            1,

            0.0,

            0
        )
