import json
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

with open("results/track_a_results.json", encoding="utf-8") as f:
    A = json.load(f)

with open("results/track_b_results.json", encoding="utf-8") as f:
    B = json.load(f)

y_true = []
y_pred = []

for x in A:
    y_true.append(0)
    y_pred.append(0 if x["prediction"] == "CORRECT" else 1)

for x in B:
    y_true.append(1)
    y_pred.append(1 if x["prediction"] == "HALLUCINATION" else 0)

cm = confusion_matrix(y_true, y_pred)

disp = ConfusionMatrixDisplay(cm)

disp.plot()

plt.savefig("results/confusion_matrix.png")

plt.show()