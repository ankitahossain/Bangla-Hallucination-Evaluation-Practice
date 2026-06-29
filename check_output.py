import json

with open("hallucinated/sample_hallucinations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for i, sample in enumerate(data):
    print("=" * 80)
    print("Sample:", i + 1)
    print("\nQuestion:")
    print(sample["question"])

    print("\nGold Answer:")
    print(sample["gold_answer"])

    print("\nHallucinated Answer:")
    print(sample["hallucinated_answer"])

    if i == 2:   # প্রথম ৩টি sample দেখাবে
        break