from transformers import DistilBertForSequenceClassification

def get_model(num_labels):
    """
    Loads DistilBERT classification model.

    Args:
        num_labels (int)

    Returns:
        model
    """
    return DistilBertForSequenceClassification.from_pretrained(
        "distilbert-base-uncased",
        num_labels=num_labels
    )