import joblib

def load_model():
    return joblib.load("models/failure_model.pkl")

def predict(data):
    model = load_model()

    values = [[data["temperature"], data["pressure"], data["vibration"]]]
    result = model.predict(values)[0]

    return result