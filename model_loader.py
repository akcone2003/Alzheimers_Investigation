import joblib

def load_model():
    model = joblib.load('models/model.pkl')
    return model

