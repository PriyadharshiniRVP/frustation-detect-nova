# Amazon Nova Powered Frustration Detection System for Developers

An AI-powered system that detects developer frustration during coding sessions using keystroke dynamics and facial emotion recognition, combined with an AI debugging assistant powered by Amazon Nova.

The system analyzes behavioral signals in real time and provides supportive guidance when frustration is detected.

---

# Problem Statement

Software developers frequently experience frustration during debugging, compilation errors, and complex problem solving. Prolonged frustration can reduce productivity, increase cognitive load, and negatively affect mental well-being.

Most development tools focus only on code correctness and performance but do not consider the emotional state of the developer.

This project aims to build an emotion-aware development support system that can:

* Detect developer frustration in real time
* Analyze behavioral and emotional signals
* Provide supportive debugging assistance
* Encourage healthier coding practices

---

# Solution Overview

The system integrates behavioral analytics, computer vision, machine learning, and cloud-based AI assistance.

Core components include:

* Keystroke dynamics analysis
* Facial emotion recognition
* Multimodal frustration classification using LightGBM
* Real-time frustration monitoring
* AI-powered debugging assistant using Amazon Nova
* Interactive support popup called CodeBuddy

When frustration is detected, the system launches an AI assistant that provides debugging suggestions and encouragement.

---

# System Architecture

The system follows a multimodal detection pipeline:

Keystroke Logger
+
Facial Emotion Detection
↓
Feature Extraction
↓
LightGBM Fusion Model
↓
Frustration Probability
↓
If frustration detected
↓
CodeBuddy Popup Assistant
↓
Amazon Nova AI Response

---

# Project Components

## 1. Keystroke Logger

Captures behavioral typing signals including:

* Typing speed
* Backspace frequency
* Pause intervals
* Burst typing patterns

These signals help detect behavioral signs of frustration.

---

## 2. Facial Emotion Detection

Uses computer vision to estimate emotional state based on facial expressions.

Technologies used:

* OpenCV
* MediaPipe
* TensorFlow

The model outputs emotion probability scores that contribute to frustration detection.

---

## 3. Multimodal Fusion Engine

A LightGBM model combines:

* Keystroke behavioral features
* Facial emotion probabilities

to estimate the probability that a developer is experiencing frustration.

Example output:

P_keystroke: 0.93
P_face: 0.12
P_total: 0.67
frustrated: True

---

## 4. CodeBuddy AI Assistant

When frustration is detected, the system launches an interactive assistant called CodeBuddy.

Features:

* Chat-based debugging assistance
* Quick troubleshooting suggestions
* Encouraging developer feedback
* Lightweight popup interface

The assistant helps developers recover quickly from debugging difficulties.

---

## 5. Amazon Nova Integration

The AI assistant is powered by Amazon Nova through AWS Bedrock.

Nova provides:

* Natural language debugging guidance
* Problem explanation
* Short troubleshooting advice
* Encouraging developer feedback

This allows the system to act as an AI pair-programming companion.

---

# Project Structure

amazon-nova-frust/

App/
│ app.py
│ fusion_engine.py
│ keystroke_logger.py
│ facial_logger.py
│ cute_popup.py
│ nova_assistant.py

models/
│ keystroke_model.pkl
│ fusion_model.pkl

training/
│ train_keystroke_model.py
│ train_fusion_model.py

training_data/
│ keystroke_dataset.csv
│ processed_data.csv

README.md

---

# Technology Stack

Programming

* Python

Machine Learning

* LightGBM
* Scikit-learn
* Joblib

Computer Vision

* OpenCV
* MediaPipe
* TensorFlow

AI Integration

* AWS Bedrock
* Amazon Nova

Interface

* Tkinter popup assistant

---

# Dataset Structure

Example feature structure used for training the keystroke model:

typing_speed | backspace_count | pause_count | avg_pause | burst_ratio | label

Label Encoding

0 → Calm
1 → Frustrated

---

# Ethical Considerations

The system is designed with responsible data practices.

* No source code content is stored
* Only behavioral metadata is analyzed
* Facial data is processed locally
* No biometric data is permanently stored
* User consent is required before monitoring

---

# Future Enhancements

Potential improvements include:

* IDE integration (VS Code extension)
* Real-time error trace analysis
* Deep learning based multimodal fusion
* Multi-user team analytics dashboard
* Stress trend visualization
* Smart break recommendation system

---

# Vision

To build emotionally intelligent development environments that support both developer productivity and well-being.

The long-term goal is to create AI systems that understand the human side of programming and assist developers when cognitive overload or frustration occurs.

---

# Author

Priyadharshini R
B.E. Computer Science and Engineering
Specialization: Cloud Computing and Data Center Technologies

---

# License

This project is developed for academic and research purposes.
