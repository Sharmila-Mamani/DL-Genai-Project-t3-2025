---
title: Emotion Bert App
emoji: 💻
colorFrom: yellow
colorTo: blue
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
---
<h2 style="color:#2C3E50;">
Emotion Classification with BERT
</h2>

<p style="font-size:15px;">
This Hugging Face Space hosts an <strong>interactive multi-label emotion classification</strong>
web application powered by a fine-tuned
<strong>BERT (bert-base-uncased)</strong> model.
</p>

<p style="font-size:15px;">
The model predicts five emotions from English text:
<strong>Anger</strong>, <strong>Fear</strong>,
<strong>Joy</strong>, <strong>Sadness</strong>, and
<strong>Surprise</strong>.  
Multiple emotions may be present in a single input.
</p>

<hr/>

<h3 style="color:#1F618D;">
Model & Training Summary
</h3>

<ul style="font-size:15px; line-height:1.6;">
  <li><strong>Architecture:</strong> BERT (bert-base-uncased) + custom classification head</li>
  <li><strong>Framework:</strong> PyTorch & Hugging Face Transformers</li>
  <li><strong>Task:</strong> Multi-label emotion classification</li>
  <li><strong>Evaluation Metric:</strong> Macro F1-score</li>
  <li><strong>Best Performance:</strong>
    <ul>
      <li>Validation Macro F1 ≈ <strong>0.88</strong></li>
      <li>Kaggle Public Leaderboard F1 ≈ <strong>0.85</strong></li>
    </ul>
  </li>
</ul>

<hr/>

<h3 style="color:#117A65;">
Deployment Details
</h3>

<ul style="font-size:15px; line-height:1.6;">
  <li><strong>Platform:</strong> Hugging Face Spaces</li>
  <li><strong>UI Framework:</strong> Gradio</li>
  <li><strong>Backend:</strong> PyTorch</li>
  <li><strong>Execution:</strong> On-demand (app sleeps when idle)</li>
</ul>

<hr/>

<h3 style="color:#9C640C;">
How to Use
</h3>

<ol style="font-size:15px; line-height:1.6;">
  <li>Enter a sentence in the input box</li>
  <li>Click <strong>Submit</strong></li>
  <li>View predicted emotion probabilities</li>
</ol>

<hr/>

<h3 style="color:#884EA0;">
💬 Example Inputs
</h3>

<ul style="font-size:15px; line-height:1.6;">
  <li><em>"I am very happy and excited today!"</em></li>
  <li><em>"I feel nervous and scared about the exam."</em></li>
  <li><em>"That movie made me sad but also hopeful."</em></li>
</ul>

<hr/>

<p style="font-size:14px;">
<strong>Status:</strong> Live & Stable<br/>
<strong>Purpose:</strong> Academic Project Demonstration
</p>


Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
