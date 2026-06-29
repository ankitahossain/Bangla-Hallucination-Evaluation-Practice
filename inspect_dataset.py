import json

with open("datasets/qa/bn_train.json", "r", encoding="utf-8") as f:
    sample = json.loads(f.readline())

print(sample)