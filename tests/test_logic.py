import unittest
import numpy as np
from src.detector import DrowsinessDetector
from src.alerts import ScoringSystem

class TestDetectionLogic(unittest.TestCase):
    def setUp(self):
        self.detector = DrowsinessDetector()
        self.scoring = ScoringSystem()

    def test_calculate_ear(self):
        # Mock eye landmarks for an open eye
        # Points: [left, top_left, top_right, right, bottom_right, bottom_left]
        eye_open = np.array([
            [0, 5], [2, 10], [8, 10], [10, 5], [8, 0], [2, 0]
        ])
        ear = self.detector.calculate_ear(eye_open)
        # (10 + 10) / (2 * 10) = 1.0
        self.assertAlmostEqual(ear, 1.0)

    def test_calculate_mar(self):
        # Mock mouth landmarks
        mouth = np.array([
            [0, 5], [10, 5], [5, 15], [5, 15], [5, -5], [5, -5]
        ])
        mar = self.detector.calculate_mar(mouth)
        # (20 + 20) / (2 * 10) = 2.0
        self.assertAlmostEqual(mar, 2.0)

    def test_scoring_increments(self):
        # Test that score increments when EAR is below threshold
        self.scoring.ear_threshold = 0.5
        is_drowsy, _, _ = self.scoring.update(0.1, 0.1, 0.1)
        self.assertEqual(self.scoring.drowsiness_counter, 1)
        self.assertFalse(is_drowsy)

if __name__ == '__main__':
    unittest.main()
