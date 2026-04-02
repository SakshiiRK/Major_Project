from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class Predictor:
    def __init__(self, model_path):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_path)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)
        self.model.eval()

    def predict(self, text, label_map):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits
        pred = torch.argmax(logits, dim=1).item()

        return label_map[pred]