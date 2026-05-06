import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification


class Predictor:
    def __init__(self, model_path):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_path)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_path)
        self.model.eval()

    def predict(self, text, labels):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)

        with torch.no_grad():
            outputs = self.model(**inputs)

        pred = torch.argmax(outputs.logits).item()
        return labels[pred]