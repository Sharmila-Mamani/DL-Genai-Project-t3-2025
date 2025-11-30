import os
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertModel
import gradio as gr

# ---------------------------
# Config
# ---------------------------
MODEL_DIR = "emotion-bert-uncased-v2"
MODEL_NAME = "bert-base-uncased"
LABELS = ["anger", "fear", "joy", "sadness", "surprise"]
MAX_LEN = 80

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------
# Model definition
#   IMPORTANT: use "linear" (not "classifier")
#   to match your trained checkpoint.
# ---------------------------
class BertForMultiLabel(nn.Module):
    def __init__(self, model_name, num_labels):
        super().__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.dropout = nn.Dropout(0.3)
        self.linear = nn.Linear(self.bert.config.hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled = outputs.pooler_output
        pooled = self.dropout(pooled)
        logits = self.linear(pooled)
        return logits  # raw logits (we'll apply sigmoid in predict)


# ---------------------------
# Load tokenizer and model
# ---------------------------
tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)

model = BertForMultiLabel(MODEL_NAME, num_labels=len(LABELS)).to(device)
state_dict = torch.load(
    os.path.join(MODEL_DIR, "pytorch_model.bin"),
    map_location=device
)
model.load_state_dict(state_dict)  # now keys match ("linear.*")
model.eval()

# ---------------------------
# Prediction function
# ---------------------------
def predict(text):
    if not text or text.strip() == "":
        return {label: 0.0 for label in LABELS}

    enc = tokenizer(
        text,
        max_length=MAX_LEN,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )

    input_ids = enc["input_ids"].to(device)
    attention_mask = enc["attention_mask"].to(device)

    with torch.no_grad():
        logits = model(input_ids, attention_mask)
        probs = torch.sigmoid(logits).cpu().numpy()[0]

    # Return probabilities as float (0–1)
    return {label: float(p) for label, p in zip(LABELS, probs)}

# ---------------------------
# Gradio Interface
# ---------------------------
demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter text here..."
    ),
    outputs=gr.Label(num_top_classes=5),
    title="Emotion Classifier (BERT)",
    description="Multi-label emotion classification using fine-tuned bert-base-uncased"
)

demo.launch()
