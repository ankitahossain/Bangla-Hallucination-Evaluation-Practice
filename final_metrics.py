import json
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

with open("results/track_a_results.json",encoding="utf-8") as f:
    trackA=json.load(f)

with open("results/track_b_results.json",encoding="utf-8") as f:
    trackB=json.load(f)

y_true=[]
y_pred=[]

# Track A
for item in trackA:
    y_true.append(0)
    y_pred.append(0 if item["prediction"]=="CORRECT" else 1)

# Track B
for item in trackB:
    y_true.append(1)
    y_pred.append(1 if item["prediction"]=="HALLUCINATION" else 0)

print("="*60)

print("Accuracy :",accuracy_score(y_true,y_pred))
print("Precision:",precision_score(y_true,y_pred))
print("Recall   :",recall_score(y_true,y_pred))
print("F1 Score :",f1_score(y_true,y_pred))

print()

print(confusion_matrix(y_true,y_pred))