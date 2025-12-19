Driver Drowsiness Detection System
==================================


A modernized, high-performance driver drowsiness detection system using **MediaPipe** and **Streamlit**.

Features
--------
- **Accurate Tracking**: Uses MediaPipe Face Mesh for sub-pixel ocular and oral tracking.
- **Robust Metrics**:
    - **EAR (Eye Aspect Ratio)**: For optimized blink and sustained closure detection.
    - **MAR (Mouth Aspect Ratio)**: For early-onset fatigue detection via yawning analysis.
    - **Head Pitch Estimation**: Detects "head slumping" forward, a critical indicator of deep sleep.
- **Enterprise-Grade Architecture**: Modular Python structure with comprehensive docstrings.
- **Real-time Dashboard**: Streamlit interface with live telemetry and historical trend analysis.
- **Containerized**: Full Docker support for platform-agnostic deployment.
- **Verified**: Integrated unit test suite for algorithmic validation.

Tech Stack
----------
- **Core**: Python 3.9+
- **Vision**: MediaPipe, OpenCV
- **UI**: Streamlit, Plotly
- **Math**: NumPy, SciPy
- **Audio**: Pygame
- **Testing**: Unittest
- **Deployment**: Docker

Installation and Deployment
---------------------------

Standard Installation
~~~~~~~~~~~~~~~~~~~~~
1. Clone the repository:
   ```bash
   git clone https://github.com/sandeeplingam1/Driver-Drowsiness-Detection
   cd Driver-Drowsiness-Detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Docker Deployment (Recommended for Portability)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To run the system in a containerized environment:
```bash
docker build -t drowsiness-detection .
docker run -p 8501:8501 --device /dev/video0:/dev/video0 drowsiness-detection
```

Usage and Operation Guide
-------------------------

Running the System
~~~~~~~~~~~~~~~~~~
To initiate the detection dashboard, execute:
```bash
streamlit run app.py
```

System Configuration
~~~~~~~~~~~~~~~~~~~~
Parameters accessible via the sidebar telemetry control:
1. **EAR Threshold**: Sensitivity for ocular closure.
2. **MAR Threshold**: Sensitivity for yawning analysis.
3. **Pitch Threshold**: Sensitivity for head-slump detection.

Automated Validation
--------------------
To run the internal logic tests:
```bash
python3 -m unittest discover tests
```

How it Works
------------
The system orchestrates three primary volumetric metrics:
- **EAR**: Measures eye aperture.
- **MAR**: Measures oral expansion.
- **Pitch**: Measures vertical head orientation.

A temporal scoring system monitors these metrics; if thresholds are breached for a configurable duration, the system dispatches visual and audible alerts to the operator.

License
-------
MIT
