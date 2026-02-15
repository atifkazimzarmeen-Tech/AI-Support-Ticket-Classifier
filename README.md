# AI-Support-Ticket-Classifier
AI-powered support ticket classification system using NLP and Large Language Models to automatically assign top-3 relevant tags via zero-shot and few-shot learning.
An end-to-end NLP-based web application that automatically classifies customer support tickets into relevant categories using Zero-Shot Learning with Large Language Models (LLMs).

Built with Flask + Hugging Face Transformers, this project demonstrates real-world implementation of Natural Language Processing for business automation.

 Project Overview

Customer support systems receive thousands of tickets daily.
Manually categorizing them is time-consuming and inefficient.

This system uses Zero-Shot Classification powered by the facebook/bart-large-mnli model to automatically assign the most relevant tags — without requiring custom model training.

 Features

 Zero-shot text classification

 Automatic tag prediction

 Confidence score display

 Modern Flask web interface

 Real-time AI inference

 Easy-to-modify label categories

 Tech Stack

Python

Flask

Hugging Face Transformers

PyTorch

HTML5

CSS3

 Project Structure
AI-Support-Ticket-Classifier/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md

 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️ Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000/

 Example Test Inputs

Try entering tickets like:

I was charged twice for my subscription. Please refund the extra amount.

My internet connection is not working since yesterday.

How can I upgrade my current plan?

 Example Categories

You can customize categories inside app.py:

Billing Issue

Technical Support

Account Management

Refund Request

General Inquiry

 Model Used

facebook/bart-large-mnli

Zero-Shot Classification Pipeline

Provided by Hugging Face

 Future Improvements

Fine-tuned model on custom dataset

Authentication system

Admin analytics dashboard

Cloud deployment (Render / AWS / Railway)

Docker containerization

 Demo

(Add your screenshot inside a screenshots folder and link it here)

screenshots/demo.png

 Author

AI/ML Enthusiast building real-world NLP applications using modern AI frameworks.
