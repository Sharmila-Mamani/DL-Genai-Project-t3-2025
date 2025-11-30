# DL-Genai-Project-t3-2025
This repository is for IIT DL and GenAI project.

Project Title: 2025 Sep DLGenAI Project
Name : Sharmila M
ID   : 24ds2000048

# Multi-Label Emotion Classification using Deep Learning and Transformers

## Project Description
Emotions in natural language are often subtle, overlapping, and context-dependent.  
This project focuses on **multi-label emotion classification**, where each text input may express multiple emotions simultaneously.

The goal is to predict the presence of five emotions from short English text:
- **Anger**
- **Fear**
- **Joy**
- **Sadness**
- **Surprise**

This is a **multi-label classification problem**, evaluated using **Macro F1-Score**.  
The project explores neural and transformer-based models to progressively improve performance and understanding of contextual language representations.

---

## Dataset
- **Input:** Short English text
- **Output:** Binary labels for each of the five emotions
- **Task Type:** Multi-label classification
- **Evaluation Metric:** Macro F1-Score (averaged across all emotions)

---

## Selected Models (Final)
Three models were selected to satisfy the project requirements and to demonstrate progression from simpler neural models to pretrained transformers.

### 1. MLPClassifier (Neural Baseline)
- Uses TF-IDF text representations
- Feed-forward neural network (MLP)
- Serves as a neural baseline for comparison

### 2. BiLSTM (Built from Scratch)
- Implemented fully in **PyTorch**
- Trained from random initialization (no pretrained embeddings)
- Captures sequential and contextual dependencies in text
- Satisfies the *model built from scratch* requirement

### 3. BERT (Pretrained Transformer)
- Fine-tuned **bert-base-uncased**
- Leverages contextual embeddings learned from large corpora
- Highest performing model
- Deployed as an interactive application

---

## Project Structure

- `notebooks/experiments/` contains all experimentation notebooks.
- `notebooks/final/` contains only the three selected models used for evaluation and reporting.


---

## Model Evaluation Summary

| Model | Type | Macro F1 (Validation) | Kaggle Public Score |
|-----|-----|----------------------|-------------------|
| MLPClassifier | Neural baseline | ~0.73 | ~0.71 |
| BiLSTM | From scratch | ~0.72 | ~0.71 |
| BERT | Pretrained transformer | ~0.88 | ~0.85 |

---

## Deployment
The best-performing model (**BERT**) is deployed as an interactive web application using **Hugging Face Spaces** and **Gradio**.

🔗 **Deployment Link:**  
https://huggingface.co/spaces/sharmilamamani/emotion-bert-app

The application allows users to input text and view real-time emotion probability predictions.  
The deployment runs on an on-demand basis and sleeps when idle.

---

## Tools & Technologies
- Python
- PyTorch
- scikit-learn
- Hugging Face Transformers
- Gradio
- Kaggle
- Git & GitHub

---

## Conclusion
This project demonstrates how increasingly sophisticated neural architectures improve performance on multi-label emotion classification tasks.  
Starting from a neural baseline, progressing through a custom BiLSTM, and culminating in a pretrained transformer, the results clearly show the advantages of contextual language modeling.

---

## Author
**Sharmila Mamani**

