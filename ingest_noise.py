import psycopg2
import time
import random

def stream_noise_data():
    # Connect to your new noise_db
    conn = psycopg2.connect("dbname=noise_db user=Omistaja host=localhost")
    cur = conn.cursor()
    
    sensors = ['SNSR-001', 'SNSR-002', 'SNSR-003']
    print("Streaming noise measurements to PostgreSQL...")

    while True:
        for s_id in sensors:
            # Simulate urban noise (dB levels)
            db_level = random.uniform(45.0, 85.0)
            cur.execute(
                "INSERT INTO noise_readings (sensor_id, db_level) VALUES (%s, %s)",
                (s_id, db_level)
            )
        conn.commit()
        time.sleep(5) 

if __name__ == "__main__":
    stream_noise_data()