import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/model_comparison.csv")

plt.figure(figsize=(8,5))

plt.bar(df["Model"], df["BenHalluScore"])

plt.ylabel("BenHalluScore")

plt.title("Model Comparison")

plt.savefig("results/model_comparison.png")

plt.show()