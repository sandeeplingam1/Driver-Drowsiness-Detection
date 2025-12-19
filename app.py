import streamlit as st
import cv2
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from src.detector import DrowsinessDetector
from src.alerts import AlertSystem, ScoringSystem
import time

# Page config
st.set_page_config(page_title="Driver Drowsiness Remaster", layout="wide")

st.title("Driver Drowsiness Detection System")
st.markdown("---")

# Initialize Session State
if 'detector' not in st.session_state:
    st.session_state.detector = DrowsinessDetector()
if 'alert_system' not in st.session_state:
    st.session_state.alert_system = AlertSystem("assets/alarm.wav")
if 'scoring' not in st.session_state:
    st.session_state.scoring = ScoringSystem()

# Sidebar for Settings
st.sidebar.header("Settings")
ear_thresh = st.sidebar.slider("EAR Threshold (Blink/Closed)", 0.1, 0.4, 0.25)
mar_thresh = st.sidebar.slider("MAR Threshold (Yawn)", 0.3, 1.0, 0.6)
st.session_state.scoring.ear_threshold = ear_thresh
st.session_state.scoring.mar_threshold = mar_thresh

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Live Feed")
    FRAME_WINDOW = st.image([])
    status_placeholder = st.empty()

with col2:
    st.header("Metrics & Stats")
    chart_placeholder = st.empty()
    ear_stat = st.empty()
    mar_stat = st.empty()

# Data for charts
ear_history = []
mar_history = []

cap = cv2.VideoCapture(0)

stop = st.button("Stop Session")

while not stop:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to access camera.")
        break
    
    frame = cv2.flip(frame, 1)
    ear, mar, landmarks = st.session_state.detector.process_frame(frame)
    
    if ear is not None:
        is_drowsy, is_yawning, d_counter, y_counter = st.session_state.scoring.update(ear, mar)
        
        # Display EAR and MAR history
        ear_history.append(ear)
        mar_history.append(mar)
        if len(ear_history) > 50:
            ear_history.pop(0)
            mar_history.pop(0)
            
        # UI Updates
        ear_stat.metric("Eye Aspect Ratio (EAR)", f"{ear:.2f}", delta=f"{ear - 0.25:.2f}", delta_color="inverse")
        mar_stat.metric("Mouth Aspect Ratio (MAR)", f"{mar:.2f}", delta=f"{mar - 0.6:.2f}")

        # Status logic
        if is_drowsy:
            status_placeholder.error("CRITICAL: Drowsiness Detected")
            st.session_state.alert_system.play_alarm()
        elif is_yawning:
            status_placeholder.warning("Warning: Signs of Fatigue Detected (Yawning)")
            st.session_state.alert_system.play_alarm()
        else:
            status_placeholder.success("Operator Status: Awake and Alert")

        # Visualization on frame
        # (Optional: Draw landmarks or bounding boxes here using cv2)
        
        # Plotly chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=ear_history, name="EAR", line=dict(color='blue')))
        fig.add_trace(go.Scatter(y=mar_history, name="MAR", line=dict(color='red')))
        fig.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0))
        chart_placeholder.plotly_chart(fig, use_container_width=True)

    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    time.sleep(0.01)

cap.release()
st.write("Session Stopped.")
