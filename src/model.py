import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv("data/sensor_data.csv")

    X = df[["temperature", "pressure", "vibration"]]
    y = df["failure"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/failure_model.pkl")

    print("Model trained & saved!")



if __name__ == "__main__":
    train_model()