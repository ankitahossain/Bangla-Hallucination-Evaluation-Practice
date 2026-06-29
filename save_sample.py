import json

with open("datasets/qa/bn_train.json", "r", encoding="utf-8") as f:
    sample = json.loads(f.readline())

with open("sample.json", "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=4)

print("Saved sample.json")