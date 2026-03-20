import matplotlib.pyplot as plt
from src.pipeline import run_pipeline

def main():
    df, anomalies = run_pipeline()

    print(df.tail(10))

    print("\nAnomalien:")
    print(anomalies)

    plt.scatter(
        df["temperature"],
        df["pressure"],
        c=df["anomaly"],
        cmap="coolwarm"
    )
    plt.xlabel("Temperature")
    plt.ylabel("Pressure")
    plt.title("Anomaly Detection")
    plt.show()

if __name__ == "__main__":
    main()
