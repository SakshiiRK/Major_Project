from transformers import DistilBertForSequenceClassification

def get_model(num_labels):
    return DistilBertForSequenceClassification.from_pretrained(
        "distilbert-base-uncased",
        num_labels=num_labels
    )