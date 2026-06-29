import pandas as pd

from model_loader import model

from metrics import (
    fraud_model_score,
    fraud_transaction_amount
)

# ======================================================
# 🔥 FRAUD PREDICTION ENGINE
# ======================================================

def predict_fraud(event):

    try:

        # ==================================================
        # FEATURE ENGINEERING
        # ==================================================

        amount = float(
            event["amount"]
        )

        amount_scaled = round(
            amount / 10000,
            5
        )

        risk_score = round(
            amount_scaled,
            5
        )

        # ==================================================
        # BUILD MODEL INPUT
        # ==================================================

        df = pd.DataFrame([{

            "amount_scaled": amount_scaled,

            "risk_score": risk_score
        }])

        print(
            f"🧪 Model features: "
            f"{df.to_dict(orient='records')[0]}",
            flush=True
        )

        # ==================================================
        # ML INFERENCE
        # ==================================================

        prediction = int(
            model.predict(df)[0]
        )

        probability = float(
            model.predict_proba(df)[0][1]
        )

        probability = round(
            probability,
            4
        )

        # ==================================================
        # PROMETHEUS METRICS
        # ==================================================

        fraud_model_score.set(
            probability
        )

        fraud_transaction_amount.set(
            amount
        )

        # ==================================================
        # FINAL RESPONSE
        # ==================================================

        result = {

            "user_id": event["user_id"],

            "amount": amount,

            "location": event["location"],

            "timestamp": event["timestamp"],

            "amount_scaled": amount_scaled,

            "risk_score": risk_score,

            "fraud_prediction": prediction,

            "fraud_probability": probability
        }

        # ==================================================
        # LOGGING
        # ==================================================

        print(
            f"🧠 ML Prediction → "
            f"probability={probability}, "
            f"prediction={prediction}",
            flush=True
        )

        return result

    except Exception as e:

        print(
            f"❌ Prediction failed: {e}",
            flush=True
        )

        return {

            "user_id": event.get("user_id"),

            "amount": event.get("amount"),

            "location": event.get("location"),

            "timestamp": event.get("timestamp"),

            "fraud_prediction": 0,

            "fraud_probability": 0.0,

            "error": str(e)
        }
