import random
from datetime import datetime

def generate_transaction():
    return {
        "user_id": random.randint(1, 1000),
        "amount": random.randint(10, 10000),
        "location": random.choice(["IN", "US", "UK"]),
        "timestamp": str(datetime.utcnow())
    }
