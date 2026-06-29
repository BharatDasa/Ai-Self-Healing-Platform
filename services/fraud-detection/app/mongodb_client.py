from pymongo import MongoClient
from pymongo.errors import PyMongoError

from metrics import mongodb_writes_total

# ======================================================
# 🔥 MONGODB CONFIG
# ======================================================

MONGO_URI = (
    "mongodb://mongodbAdmin:Admin123@mongodb.databases.svc.cluster.local:27017/"
)

DATABASE_NAME = "fraud_detection"

FRAUD_COLLECTION = "fraud_events"

PREDICTION_COLLECTION = "predictions"

# ======================================================
# 🔥 CONNECT TO MONGODB
# ======================================================

try:

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    fraud_collection = db[FRAUD_COLLECTION]

    prediction_collection = db[PREDICTION_COLLECTION]

    print(
        "✅ Connected to MongoDB",
        flush=True
    )

except Exception as e:

    print(
        f"❌ MongoDB connection failed: {e}",
        flush=True
    )

    raise

# ======================================================
# 🔥 STORE RAW FRAUD EVENT
# ======================================================

def save_fraud_event(event):

    try:

        fraud_collection.insert_one(dict(event))

        mongodb_writes_total.inc()

        print(
            "🍃 Fraud event stored",
            flush=True
        )

    except PyMongoError as e:

        print(
            f"❌ Failed to store fraud event: {e}",
            flush=True
        )

# ======================================================
# 🔥 STORE ML PREDICTION
# ======================================================

def save_prediction(prediction):

    try:

        prediction_collection.insert_one(
            dict(prediction)
        )

        mongodb_writes_total.inc()

        print(
            "🧠 Prediction stored",
            flush=True
        )

    except PyMongoError as e:

        print(
            f"❌ Failed to store prediction: {e}",
            flush=True
        )
