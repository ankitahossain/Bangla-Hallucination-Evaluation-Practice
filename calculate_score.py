track_a_error = 0.40
track_b_error = 0.20

benhallu_score = (track_a_error + track_b_error) / 2

print("=" * 40)
print("BenHalluEval Results")
print("=" * 40)
print(f"Track A Error : {track_a_error:.2f}")
print(f"Track B Error : {track_b_error:.2f}")
print(f"BenHalluScore: {benhallu_score:.2f}")