import joblib

MODEL_PATH = "models/scaling_model.pkl"

model = joblib.load(MODEL_PATH)

print("✅ Scaling ML model loaded")
