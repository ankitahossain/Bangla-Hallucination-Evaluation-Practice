import json

with open("results/track_a_results.json",encoding="utf-8") as f:
    A=json.load(f)

with open("results/track_b_results.json",encoding="utf-8") as f:
    B=json.load(f)

trackA=sum(1 for x in A if x["prediction"]=="CORRECT")/len(A)

trackB=sum(1 for x in B if x["prediction"]=="HALLUCINATION")/len(B)

trackA_error=1-trackA
trackB_error=1-trackB

score=(trackA_error+trackB_error)/2

print("="*60)

print("Track A Accuracy :",trackA)
print("Track B Accuracy :",trackB)

print()

print("Track A Error :",trackA_error)
print("Track B Error :",trackB_error)

print()

print("BenHalluScore :",score)