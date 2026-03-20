import logging
from src.generate import generate_data
from src.detect import detect_anomalies
from src.storage import save_to_sqlite

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("Starte Pipeline...")

    df = generate_data()

    logging.info("Erkenne Anomalien...")
    df = detect_anomalies(df)

    logging.info("Speichere Daten...")

    df.to_csv("data/raw_data.csv", index=False)

    anomalies = df[df["anomaly"] == -1]
    anomalies.to_csv("data/anomalies.csv", index=False)

    save_to_sqlite(df)
    logging.info("Datenbank gespeichert: data/anomaly_data.db")

    logging.info("Pipeline erfolgreich abgeschlossen.")

    return df, anomalies
