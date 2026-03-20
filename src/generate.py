import pandas as pd
import numpy as np

def generate_data(n=200):
    np.random.seed(42)

    df = pd.DataFrame({
        "temperature": np.random.normal(50, 5, n),
        "pressure": np.random.normal(100, 10, n),
        "vibration": np.random.normal(30, 3, n),
        "humidity": np.random.normal(60, 5, n)
    })

    anomalies = pd.DataFrame({
        "temperature": [80, 85, 90],
        "pressure": [150, 160, 170],
        "vibration": [60, 65, 70],
        "humidity": [90, 95, 100]
    })

    df = pd.concat([df, anomalies], ignore_index=True)

    return df
