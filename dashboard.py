import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

st.title(" Helsinki Noise Pollution Monitor")

# Fetch data from the structured database
conn = psycopg2.connect("dbname=noise_db user=Omistaja host=localhost")
query = """
    SELECT r.db_level, r.recorded_at, s.latitude, s.longitude, s.location_name
    FROM noise_readings r
    JOIN acoustic_sensors s ON r.sensor_id = s.sensor_id
    ORDER BY r.recorded_at DESC LIMIT 100
"""
df = pd.read_sql(query, conn)

# Map Layer
st.subheader("Sensor Hotspots")
st.map(df)

# Analytics Layer
st.subheader("Noise Trends (dB)")
fig = px.line(df, x='recorded_at', y='db_level', color='location_name')
st.plotly_chart(fig)
