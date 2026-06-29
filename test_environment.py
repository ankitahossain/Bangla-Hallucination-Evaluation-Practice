import torch
import transformers
import pandas as pd

print("Torch Version:", torch.__version__)
print("Transformers Version:", transformers.__version__)
print("Pandas Version:", pd.__version__)

print("CUDA Available:", torch.cuda.is_available())