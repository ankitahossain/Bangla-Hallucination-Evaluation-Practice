from datasets import load_dataset

print("Loading TyDiQA...")

dataset = load_dataset("tydiqa", "secondary_task")

print(dataset)