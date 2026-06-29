# Bangla-Hallucination-Evaluation-Practice

# BenHalluEval

A Bengali Hallucination Evaluation Benchmark implemented using TyDiQA Bengali and Qwen2.5.

## Features

- TyDiQA Bengali Dataset
- Hallucination Generation
- Track A Evaluation
- Track B Evaluation
- BenHalluScore
- Precision
- Recall
- F1-score
- Confusion Matrix
- CSV / Excel Export
- Model Comparison

## Models

- Qwen2.5-1.5B
- Ollama

## Requirements

Python 3.11

Install

```bash
pip install -r requirements.txt
```

Run

```bash
python scripts/generate_hallucinations.py
python scripts/evaluate.py
python scripts/evaluate_track_a.py
python scripts/final_metrics.py
python scripts/final_score.py
```
