import json
import pandas as pd

with open("results/track_a_results.json", encoding="utf-8") as f:
    trackA = json.load(f)

with open("results/track_b_results.json", encoding="utf-8") as f:
    trackB = json.load(f)

dfA = pd.DataFrame(trackA)
dfB = pd.DataFrame(trackB)

dfA.to_excel(
    "results/track_a.xlsx",
    index=False
)

dfB.to_excel(
    "results/track_b.xlsx",
    index=False
)

print("Saved Excel files.")