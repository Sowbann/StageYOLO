import json

with open("../datasets/TACO/data/annotations.json", "r") as f:
    data = json.load(f)

for cat in data["categories"]:
    print(f"ID {cat['id']}: {cat['name']}")
