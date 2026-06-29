import json
from ollama import chat

INPUT_FILE = "datasets/qa/bn_train.json"
OUTPUT_FILE = "hallucinated/four_types.json"

hallucination_types = {
    "factual": "Create a believable but factually incorrect answer.",
    "comprehension": "Misunderstand the question and answer incorrectly.",
    "specificity": "Give a vague or incomplete answer.",
    "inference": "Infer something unsupported by the context."
}

results = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i == 20:      # প্রথম ২০টি sample
            break

        sample = json.loads(line)

        item = {
            "question": sample["question"],
            "context": sample["context"],
            "gold_answer": sample["answers"]["text"][0]
        }

        for h_type, instruction in hallucination_types.items():

            prompt = f"""
Context:
{sample['context']}

Question:
{sample['question']}

Correct Answer:
{sample['answers']['text'][0]}

{instruction}

Return ONLY the answer.
"""

            response = chat(
                model="qwen2.5:1.5b",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            item[h_type] = response["message"]["content"].strip()

        results.append(item)
        print(f"Finished sample {i+1}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Saved:", OUTPUT_FILE)