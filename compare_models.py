import pandas as pd

results = {

    "Model":[
        "Qwen2.5-1.5B",
        "Gemma3-1B",
        "Llama3.2-3B"
    ],

    "Accuracy":[
        0.80,
        0.84,
        0.87
    ],

    "Precision":[
        1.00,
        0.95,
        0.96
    ],

    "Recall":[
        0.80,
        0.84,
        0.88
    ],

    "F1":[
        0.889,
        0.89,
        0.92
    ],

    "BenHalluScore":[
        0.30,
        0.25,
        0.18
    ]
}

df = pd.DataFrame(results)

print(df)

df.to_csv(
    "results/model_comparison.csv",
    index=False
)