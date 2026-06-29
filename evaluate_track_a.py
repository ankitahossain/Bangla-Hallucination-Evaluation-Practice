import json
from ollama import chat

INPUT_FILE="hallucinated/sample_hallucinations.json"
OUTPUT_FILE="results/track_a_results.json"

with open(INPUT_FILE,"r",encoding="utf-8") as f:
    data=json.load(f)

results=[]

correct=0

for sample in data:

    prompt=f"""
Question:
{sample['question']}

Answer:
{sample['gold_answer']}

Reply ONLY

CORRECT

or

HALLUCINATION
"""

    response=chat(
        model="qwen2.5:1.5b",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    prediction=response["message"]["content"].strip()

    if prediction=="CORRECT":
        correct+=1

    results.append({
        "question":sample["question"],
        "answer":sample["gold_answer"],
        "prediction":prediction
    })

with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
    json.dump(results,f,ensure_ascii=False,indent=4)

print("Track A Accuracy:",correct/len(data))
print("Saved:",OUTPUT_FILE)