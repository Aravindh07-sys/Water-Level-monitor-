
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Simulated data
current_water_level = 28  # in percentage
last_fill_date = datetime(2025, 8, 31, 14, 0)
last_drop_date = datetime(2025, 9, 2, 6, 0)
timestamps = pd.date_range(end=datetime.now(), periods=50, freq='H')
pressure_data = np.random.normal(loc=100, scale=5, size=50)
volume_data = np.linspace(500, 300, 50)  # Simulated drop

# Title
st.title("💧 Water Tank Monitoring Dashboard")

# Tank Gauge
gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_water_level,
    title={'text': "Current Water Level (%)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "blue"},
        'steps': [
            {'range': [0, 30], 'color': "red"},
            {'range': [30, 70], 'color': "yellow"},
            {'range': [70, 100], 'color': "green"}
        ],
    }
))
st.plotly_chart(gauge_fig)

# Error popups
if current_water_level <= 30:
    st.error("⚠️ Water level is critically low. Please refill the tank.")

if volume_data[-2] - volume_data[-1] > 50:
    st.error("⚠️ Sudden drop in water level detected!")

# Historical Data
col1, col2 = st.columns(2)
col1.metric("Last Fill Date", last_fill_date.strftime("%Y-%m-%d %H:%M"))
col2.metric("Last Water Level Drop", last_drop_date.strftime("%Y-%m-%d %H:%M"))

# Sensor Stability Graph
st.subheader("📈 Sensor Stability Over Time")
st.line_chart(pd.DataFrame({'Pressure (kPa)': pressure_data}, index=timestamps))

# Water Volume Trend Graph
st.subheader("📊 Water Volume Trend")
st.line_chart(pd.DataFrame({'Volume (Liters)': volume_data}, index=timestamps))
