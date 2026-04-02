import pandas as pd
from transformers import DistilBertTokenizer, Trainer, TrainingArguments
from sklearn.preprocessing import LabelEncoder
from .model import get_model
import torch


class LessonDataset(torch.utils.data.Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.encodings = tokenizer(texts, truncation=True, padding=True)
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


def train_model(csv_path, target_col, model_save_path):
    df = pd.read_csv(csv_path)

    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

    le = LabelEncoder()
    labels = le.fit_transform(df[target_col])

    dataset = LessonDataset(df["text"].tolist(), labels, tokenizer)

    model = get_model(len(le.classes_))

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        logging_dir="./logs",
        save_strategy="no"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    trainer.train()

    model.save_pretrained(model_save_path)
    tokenizer.save_pretrained(model_save_path)

    print(f"{target_col} model trained and saved.")