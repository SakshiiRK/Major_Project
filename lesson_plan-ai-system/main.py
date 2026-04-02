from src.data_processing.dataset import build_dataset
from src.training.train import train_model

# Step 1: Build dataset
build_dataset("data/raw/lessons.txt", "data/processed/dataset.csv")

# Step 2: Train Bloom model
train_model(
    "data/processed/dataset.csv",
    target_col="bloom",
    model_save_path="models/bloom_model"
)

# Step 3: Train Teaching Style model
train_model(
    "data/processed/dataset.csv",
    target_col="style",
    model_save_path="models/style_model"
)