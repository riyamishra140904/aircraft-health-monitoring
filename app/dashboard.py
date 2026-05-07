import streamlit as st
import random
import time
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predictor import predict

st.set_page_config(page_title="Aircraft Health Monitoring", layout="wide")

st.title("✈ Aircraft Health Monitoring System")

# Store data history
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(
        columns=["temperature", "pressure", "vibration"]
    )

# Generate fake live sensor data
def generate_live_data():
    return {
        "temperature": random.uniform(50, 120),
        "pressure": random.uniform(20, 80),
        "vibration": random.uniform(0, 10)
    }

# Create placeholders
metric_placeholder = st.empty()
chart_placeholder = st.empty()

while True:

    # Generate new data
    data = generate_live_data()

    # Predict health
    result = predict(data)

    # Add new row to history
    new_row = pd.DataFrame([data])

    st.session_state.history = pd.concat(
        [st.session_state.history, new_row],
        ignore_index=True
    )

    # Keep only last 30 rows
    st.session_state.history = st.session_state.history.tail(30)

    # Show metrics
    with metric_placeholder.container():

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Temperature", f"{data['temperature']:.2f} °C")
        col2.metric("Pressure", f"{data['pressure']:.2f} PSI")
        col3.metric("Vibration", f"{data['vibration']:.2f}")

        if result == 1:
            col4.error("⚠ Failure Risk")
        else:
            col4.success("✅ Normal")

    # Show charts
    with chart_placeholder.container():

        st.subheader("📈 Live Sensor Graphs")

        st.line_chart(
            st.session_state.history[["temperature"]]
        )

        st.line_chart(
            st.session_state.history[["pressure"]]
        )

        st.line_chart(
            st.session_state.history[["vibration"]]
        )

    time.sleep(2)