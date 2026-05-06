from src.data_processing.dataset import build_dataset
from src.training.train import train_model

build_dataset("data/raw/lessons.txt", "data/processed/dataset.csv")

train_model("data/processed/dataset.csv", "bloom", "models/bloom_model")
train_model("data/processed/dataset.csv", "style", "models/style_model")