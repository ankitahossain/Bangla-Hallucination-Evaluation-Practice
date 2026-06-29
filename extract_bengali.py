from datasets import load_dataset

print("Loading dataset...")

dataset = load_dataset("tydiqa", "secondary_task")

train = dataset["train"]
validation = dataset["validation"]

# Bengali samples only
bn_train = train.filter(
    lambda x: x["id"].startswith("bengali")
)

bn_validation = validation.filter(
    lambda x: x["id"].startswith("bengali")
)

print("Bengali Train:", len(bn_train))
print("Bengali Validation:", len(bn_validation))

bn_train.to_json("datasets/qa/bn_train.json")
bn_validation.to_json("datasets/qa/bn_validation.json")

print("Done.")