import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist

class DrowsinessDetector:
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
        self.MOUTH = [61, 291, 37, 267, 0, 17] # Simplified indices for MAR

    def calculate_ear(self, eye_landmarks):
        # eye_landmarks is a list of 6 points
        # dist(p2, p6), dist(p3, p5)
        # Vertical distances
        A = dist.euclidean(eye_landmarks[1], eye_landmarks[5])
        B = dist.euclidean(eye_landmarks[2], eye_landmarks[4])
        # Horizontal distance
        C = dist.euclidean(eye_landmarks[0], eye_landmarks[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def calculate_mar(self, mouth_landmarks):
        # Simplified MAR calculation
        # Vertical distance
        A = dist.euclidean(mouth_landmarks[2], mouth_landmarks[4]) # top, bottom
        B = dist.euclidean(mouth_landmarks[3], mouth_landmarks[5]) # top, bottom
        # Horizontal distance
        C = dist.euclidean(mouth_landmarks[0], mouth_landmarks[1]) # left, right
        mar = (A + B) / (2.0 * C)
        return mar

    def process_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        if not results.multi_face_landmarks:
            return None, None, None

        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = frame.shape

        def get_coords(idx_list):
            return np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in idx_list])

        left_eye_pts = get_coords(self.LEFT_EYE)
        right_eye_pts = get_coords(self.RIGHT_EYE)
        mouth_pts = get_coords(self.MOUTH)

        ear_l = self.calculate_ear(left_eye_pts)
        ear_r = self.calculate_ear(right_eye_pts)
        ear = (ear_l + ear_r) / 2.0
        
        mar = self.calculate_mar(mouth_pts)

        return ear, mar, results.multi_face_landmarks[0]
