-- schema.sql
CREATE TABLE acoustic_sensors (
    sensor_id VARCHAR(10) PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    location_name VARCHAR(50)
);

CREATE TABLE noise_readings (
    reading_id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(10) REFERENCES acoustic_sensors(sensor_id),
    db_level FLOAT NOT NULL,
    recorded_at TIMESTAMPTZ DEFAULT NOW()
);

-- Insert baseline sensors in Helsinki
INSERT INTO acoustic_sensors (sensor_id, latitude, longitude, location_name) VALUES
('SNSR-001', 60.1699, 24.9384, 'Kamppi'),
('SNSR-002', 60.1841, 24.9493, 'Kallio'),
('SNSR-003', 60.1867, 24.8281, 'Otaniemi');