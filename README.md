Driver Drowsiness Detection System
==================================


A modernized, high-performance driver drowsiness detection system using **MediaPipe** and **Streamlit**.

Features
--------
- **Accurate Tracking**: Uses MediaPipe Face Mesh for sub-pixel eye and mouth tracking.
- **Robust Metrics**:
    - **EAR (Eye Aspect Ratio)** for blink and sleep detection.
    - **MAR (Mouth Aspect Ratio)** for yawn detection.
- **Real-time Dashboard**: Interactive Streamlit UI with live metrics and historical plots.
- **Scoring System**: Intelligent scoring to reduce false positives.
- **Audio Alerts**: Audible alarms when critical fatigue levels are detected.

Tech Stack
----------
- **Core**: Python 3.9+
- **Vision**: MediaPipe, OpenCV
- **UI**: Streamlit, Plotly
- **Math**: NumPy, SciPy
- **Audio**: Pygame

Installation
------------

1. Clone the repository:
   ```bash
   git clone https://github.com/sandeeplingam1/Driver-Drowsiness-Detection
   cd Driver-Drowsiness-Detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Add your own alarm sound:
   Place a file named `alarm.wav` in the `assets/` directory.

Usage and Operation Guide
-------------------------

Running the System
~~~~~~~~~~~~~~~~~~
To initiate the detection dashboard, execute the following command in your terminal:

```bash
streamlit run app.py
```

System Configuration
~~~~~~~~~~~~~~~~~~~~
Upon launching the dashboard, the following parameters can be adjusted via the sidebar:

1. **EAR Threshold**: Sets the sensitivity for eye-closure detection. 
   - Increase this if the system fails to detect eye closure.
   - Decrease this if the system triggers false alarms during normal blinking.

2. **MAR Threshold**: Sets the sensitivity for yawn detection.
   - Adjust based on individual facial geometry and camera distance.

Operational Best Practices
~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Lighting**: Ensure the face is well-illuminated. Avoid strong backlighting which can obscure facial features.
- **Camera Position**: For optimal results, position the camera at eye level, directly in front of the operator.
- **Hardware Access**: The application requires browser-level permission to access the system webcam. Ensure these permissions are granted when prompted.

Visual Telemetry
~~~~~~~~~~~~~~~~
The dashboard provides a real-time Plotly graph showing temporal trends for EAR and MAR. This allows for objective monitoring of alertness levels over the duration of the session.

How it Works
------------
The system calculates the **Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)**. 
- If the EAR falls below a certain threshold for a sustained period, it triggers a "Drowsy" alert.
- If the MAR exceeds a threshold, it triggers a "Yawn" warning.
- A scoring system increments during fatiguing behavior and decrements during normal behavior to ensure reliability.

License
-------
MIT
