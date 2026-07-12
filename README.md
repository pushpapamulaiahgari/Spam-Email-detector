# 📧 Spam Email Detector

An ML-powered web application that classifies emails/messages as **Spam** or **Not Spam** using Natural Language Processing.

## 🚀 Live Demo
https://spam-email-detector-x5sy.onrender.com

## ✨ Features
- Real-time spam detection for any text input
- Clean and responsive UI
- Trained on real email dataset
- Deployed on Render with Flask backend

## 🛠️ Tech Stack
**Frontend**: HTML, CSS  
**Backend**: Python, Flask  
**ML/DL**: Scikit-learn, Pandas, NumPy, TF-IDF Vectorizer, Naive Bayes  
**Deployment**: Render, Gunicorn  
**Model Saving**: Joblib

## 📊 How it Works
1.  Text input is preprocessed - lowercasing, removing stopwords
2.  TF-IDF Vectorizer converts text to numerical features
3.  Trained Naive Bayes model predicts if the message is Spam or Not Spam

## ⚙️ Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/pushpapamulaiahgari/Spam-Email-detector.git
cd Spam-Email-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
