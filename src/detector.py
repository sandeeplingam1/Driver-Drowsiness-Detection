import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist

class DrowsinessDetector:
    """
    Handles facial landmark extraction and geometric metric calculations using MediaPipe.
    """
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Landmark indices for eyes and mouth
        self.LEFT_EYE = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE = [33, 160, 158, 133, 153, 144]
        self.MOUTH = [61, 291, 37, 267, 0, 17]
        self.FACE_OVAL = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]

    def calculate_ear(self, eye_landmarks):
        """
        Calculates the Eye Aspect Ratio (EAR).
        
        Args:
            eye_landmarks: Array of 6 (x, y) coordinates for an eye.
            
        Returns:
            float: The calculated EAR value.
        """
        A = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
        B = dist.euclidean(eye_landmarks[2], eye_landmarks[4])
        C = dist.euclidean(eye_landmarks[0], eye_landmarks[3])
        return (A + B) / (2.0 * C)

    def calculate_mar(self, mouth_landmarks):
        """
        Calculates the Mouth Aspect Ratio (MAR).
        
        Args:
            mouth_landmarks: Array of (x, y) coordinates for the mouth.
            
        Returns:
            float: The calculated MAR value.
        """
        A = dist.euclidean(mouth_landmarks[2], mouth_landmarks[4])
        B = dist.euclidean(mouth_landmarks[3], mouth_landmarks[5])
        C = dist.euclidean(mouth_landmarks[0], mouth_landmarks[1])
        return (A + B) / (2.0 * C)

    def get_head_pose(self, landmarks, h, w):
        """
        Estimates the head pose (pitch) using a subset of landmarks.
        
        Args:
            landmarks: MediaPipe landmarks object.
            h, w: Height and width of the frame.
            
        Returns:
            float: The estimated pitch (degree of head tilt).
        """
        # Simplified pitch estimation based on nose and chin relative position
        nose_tip = landmarks[1]
        chin = landmarks[152]
        
        # Relative vertical distance normalized by facial size
        face_top = landmarks[10].y
        face_bottom = landmarks[152].y
        face_height = face_bottom - face_top
        
        pitch = (nose_tip.y - face_top) / face_height if face_height != 0 else 0.5
        return pitch

    def process_frame(self, frame):
        """
        Processes a single video frame to extract alertness metrics.
        
        Args:
            frame: OpenCV image frame (BGR).
            
        Returns:
            tuple: (ear, mar, pitch, face_landmarks)
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        if not results.multi_face_landmarks:
            return None, None, None, None

        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = frame.shape

        def get_coords(idx_list):
            return np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in idx_list])

        ear_l = self.calculate_ear(get_coords(self.LEFT_EYE))
        ear_r = self.calculate_ear(get_coords(self.RIGHT_EYE))
        ear = (ear_l + ear_r) / 2.0
        
        mar = self.calculate_mar(get_coords(self.MOUTH))
        pitch = self.get_head_pose(landmarks, h, w)

        return ear, mar, pitch, results.multi_face_landmarks[0]
