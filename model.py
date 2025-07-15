import joblib

# Load trained model
model = joblib.load('saved_model.pkl')

def predict_news(text):
    return model.predict([text])[0]
