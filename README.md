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

Usage
-----

Run the Streamlit application:
```bash
streamlit run app.py
```

How it Works
------------
The system calculates the **Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)**. 
- If the EAR falls below a certain threshold for a sustained period, it triggers a "Drowsy" alert.
- If the MAR exceeds a threshold, it triggers a "Yawn" warning.
- A scoring system increments during fatiguing behavior and decrements during normal behavior to ensure reliability.

License
-------
MIT
