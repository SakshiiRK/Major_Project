import pandas as pd
import torch
from transformers import DistilBertTokenizer, Trainer, TrainingArguments
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pickle

from src.training.model import get_model


class LessonDataset(torch.utils.data.Dataset):
    """
    PyTorch dataset for lessons.
    """

    def __init__(self, texts, labels, tokenizer):
        self.encodings = tokenizer(
            texts,
            truncation=True,
            padding=True,
            max_length=512
        )
        self.labels = labels

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


def compute_metrics(eval_pred):
    """
    Computes accuracy for evaluation.
    """
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return {"accuracy": accuracy_score(labels, preds)}


def train_model(csv_path, target_col, save_path):
    """
    Trains DistilBERT model with evaluation.

    Args:
        csv_path (str)
        target_col (str)
        save_path (str)

    Returns:
        None
    """

    df = pd.read_csv(csv_path)

    # Clean dataset
    df = df.dropna(subset=["text"])
    df["text"] = df["text"].astype(str)
    df = df[df["text"].str.strip() != ""]

    print("Clean dataset size:", df.shape)

    # Label encoding
    le = LabelEncoder()
    labels = le.fit_transform(df[target_col])

    # Save label encoder (IMPORTANT)
    with open(f"{save_path}_label_encoder.pkl", "wb") as f:
        pickle.dump(le, f)

    # Train-test split
    X_train, X_val, y_train, y_val = train_test_split(
        df["text"].tolist(),
        labels,
        test_size=0.2,
        random_state=42
    )

    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

    train_dataset = LessonDataset(X_train, y_train, tokenizer)
    val_dataset = LessonDataset(X_val, y_val, tokenizer)

    model = get_model(len(le.classes_))

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=5,  # slightly increased
        per_device_train_batch_size=4,
        save_strategy="no",
        logging_dir="./logs",
        weight_decay=0.01
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        compute_metrics=compute_metrics
    )

    trainer.train()

    # Evaluate
    results = trainer.evaluate()
    print("Evaluation Results:", results)

    # Save model
    model.save_pretrained(save_path)
    tokenizer.save_pretrained(save_path)

    print(f"{target_col} model saved.")