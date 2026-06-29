import json
from ollama import chat

INPUT_FILE = "datasets/qa/bn_train.json"
OUTPUT_FILE = "hallucinated/sample_hallucinations.json"

results = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        if i == 100:      
            break

        sample = json.loads(line)

        context = sample["context"]
        question = sample["question"]
        answer = sample["answers"]["text"][0]

        prompt = f"""
You are creating a hallucinated answer for evaluation.

Context:
{context}

Question:
{question}

Correct Answer:
{answer}

Write ONE believable but WRONG answer.
Do not say "I don't know".
Return only the hallucinated answer.
"""

        response = chat(
            model="qwen2.5:1.5b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        hallucination = response["message"]["content"]

        results.append({
            "context": context,
            "question": question,
            "gold_answer": answer,
            "hallucinated_answer": hallucination
        })

        print(f"Finished {i+1}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Done!")