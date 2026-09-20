import json

data = {
    "studio": "Glow Beauty Studio",
    "services": [
        {"name": "Haircut", "price": 400},
        {"name": "Facial", "price": 800},
    ],
}

# Nayi service jodo
data["services"].append({"name": "Manicure", "price": 500})

# File mein save karo
with open("services.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# File se padho
with open("services.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["studio"])
for s in loaded["services"]:
    print(s["name"], "-", s["price"])
