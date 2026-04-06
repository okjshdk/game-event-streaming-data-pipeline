import random, uuid
from datetime import datetime

EVENTS = ["app_open", "login", "view_item", "purchase", "level_up"]
PLATFORMS = ["ios", "android", "web"]

def generate_event():
    event_name = random.choice(EVENTS)
    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": random.randint(1, 100000),
        "event_name": event_name,
        "platform": random.choice(PLATFORMS),
        "event_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "properties": {}
    }
    if event_name == "purchase":
        event["properties"] = {
            "item_id": f"item_{random.randint(1,50)}",
            "price": round(random.uniform(1,100),2),
            "currency": "USD"
        }
    elif event_name == "level_up":
        event["properties"] = {"level": random.randint(1,100)}
    return event