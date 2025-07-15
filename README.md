# 📰 Fake News Detector

A real-time Fake News Detector web app built using **Python**, **Streamlit**, and **NLP**.  
It classifies whether a given news article or headline is **Fake** or **Real**, using a Logistic Regression model trained on real-world news datasets.

---

## 🚀 Features

- 🔍 Paste any news text or headline to check its authenticity
- 🧠 Uses Natural Language Processing (TF-IDF) + Logistic Regression
- 📊 Trained on Kaggle dataset with both real and fake news
- 🌐 Deployed using Streamlit (runs locally in your browser)

---

## 💻 Tech Stack

- Python 🐍
- Streamlit 🌐
- Scikit-learn 🤖
- Pandas & NumPy 📊
- TF-IDF Vectorizer (NLP)
- Logistic Regression Classifier

---

## 🗂️ Dataset Source

- [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

_Note: Dataset files and trained models (`.csv`, `.pkl`) are excluded from GitHub due to size limits. Download them separately if needed._

---

## 📸 Demo Screenshots

### 🧠 App Interface
![App UI](FakeNewsDetectorSS/app(py).png)

### ⚙️ Model Code
![Model Code](FakeNewsDetectorSS/model(py).png)

### 🧪 Training the Model
![Train Model](FakeNewsDetectorSS/train_model(py).png)

### 🧹 Data Preparation
![Prepare Data](FakeNewsDetectorSS/prepare_data(py).png)

### 📂 Kaggle Dataset
![Kaggle Dataset](FakeNewsDetectorSS/kaggleDataset.png)

### 📥 Input & Output (Prediction)
![Output](FakeNewsDetectorSS/output.png)

### ❌ Prediction: Fake News
![Fake News Detected](FakeNewsDetectorSS/ifFake.png)

### ✅ Prediction: Real News
![Real News Detected](FakeNewsDetectorSS/ifReal.png)

---

## 🛠️ How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Noureesh2305/FakeNewsDetector.git
cd FakeNewsDetector
