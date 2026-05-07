import pandas as pd
import random

def generate_data(n=200):
    data = []

    for _ in range(n):
        temp = random.uniform(50, 120)
        pressure = random.uniform(20, 80)
        vibration = random.uniform(0, 10)

        
        failure = 1 if temp > 100 or vibration > 8 else 0

        data.append([temp, pressure, vibration, failure])

    df = pd.DataFrame(data, columns=["temperature", "pressure", "vibration", "failure"])
    df.to_csv("data/sensor_data.csv", index=False)

    print("Dataset created!")

if __name__ == "__main__":
    generate_data()