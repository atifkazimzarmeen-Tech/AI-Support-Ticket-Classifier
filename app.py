from flask import Flask, render_template, request
import torch
from transformers import pipeline

# ==========================
# Initialize Flask app
# ==========================
app = Flask(__name__)

# ==========================
# Load Zero-Shot Classification model
# ==========================
device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=device
)

# ==========================
# Define possible tags/categories
# ==========================
TAGS = [
    "Billing Issue",
    "Technical Bug",
    "Account Access",
    "Feature Request",
    "Refund Request",
    "Complaint",
    "Password Reset",
    "Subscription Problem",
    "Delivery Issue"
]

# ==========================
# Classification functions
# ==========================
def zero_shot_classify(text):
    """Return top 3 zero-shot predictions"""
    result = classifier(text, TAGS)
    top3 = list(zip(result["labels"][:3], result["scores"][:3]))
    return top3

def few_shot_classify(text):
    """Return top 3 few-shot predictions using a small prompt"""
    prompt_text = f"""
You are a helpful assistant for categorizing support tickets.
Classify the following ticket into one of the predefined categories.

Ticket:
{text}
"""
    result = classifier(prompt_text, TAGS)
    top3 = list(zip(result["labels"][:3], result["scores"][:3]))
    return top3

# ==========================
# Flask route for UI
# ==========================
@app.route("/", methods=["GET", "POST"])
def index():
    zero_tags = []
    few_tags = []
    ticket_text = ""

    if request.method == "POST":
        ticket_text = request.form.get("ticket_text", "")
        if ticket_text.strip():
            zero_tags = zero_shot_classify(ticket_text)
            few_tags = few_shot_classify(ticket_text)

    return render_template(
        "index.html",
        ticket_text=ticket_text,
        zero_tags=zero_tags,
        few_tags=few_tags
    )

# ==========================
# Run the Flask app
# ==========================
if __name__ == "__main__":
    # Use 127.0.0.1:5000 and debug mode ON
    app.run(debug=True)
