import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

with open("hallucinated/sample_hallucinations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ground truth:
# 1 = Hallucination
# 0 = Correct

y_true = []
y_pred = []

# এখানে আপনার বর্তমান evaluation অনুযায়ী prediction দিন
# আপাতত উদাহরণ হিসেবে ৮টি সঠিকভাবে ধরা হয়েছে
predictions = [
    "HALLUCINATION",
    "HALLUCINATION",
    "CORRECT",
    "HALLUCINATION",
    "HALLUCINATION",
    "HALLUCINATION",
    "CORRECT",
    "HALLUCINATION",
    "HALLUCINATION",
    "HALLUCINATION"
]

for pred in predictions:
    y_true.append(1)
    y_pred.append(1 if pred == "HALLUCINATION" else 0)

print("=" * 50)
print("Accuracy :", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall   :", recall_score(y_true, y_pred))
print("F1 Score :", f1_score(y_true, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_true, y_pred))