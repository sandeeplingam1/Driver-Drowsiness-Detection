import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AlertSystem:
    def __init__(self, alarm_path):
        pygame.mixer.init()
        self.alarm_path = alarm_path
        self.last_alert_time = 0
        self.cooldown = 2 # seconds
        
        if os.path.exists(alarm_path):
            self.sound = pygame.mixer.Sound(alarm_path)
        else:
            self.sound = None
            logger.warning(f"Alarm file not found at {alarm_path}")

    def play_alarm(self):
        current_time = time.time()
        if self.sound and (current_time - self.last_alert_time) > self.cooldown:
            self.sound.play()
            self.last_alert_time = current_time

class ScoringSystem:
    """
    Maintains and updates alertness scores based on temporal trends of face metrics.
    """
    def __init__(self, ear_threshold=0.25, mar_threshold=0.6, pitch_threshold=0.55, drowsiness_limit=20, yawn_limit=15):
        self.ear_threshold = ear_threshold
        self.mar_threshold = mar_threshold
        self.pitch_threshold = pitch_threshold
        self.drowsiness_counter = 0
        self.yawn_counter = 0
        self.pitch_counter = 0
        self.drowsiness_limit = drowsiness_limit
        self.yawn_limit = yawn_limit

    def update(self, ear, mar, pitch):
        """
        Updates the internal counters and checks for critical fatigue levels.
        
        Args:
            ear: Current Eye Aspect Ratio.
            mar: Current Mouth Aspect Ratio.
            pitch: Current head pitch estimation.
            
        Returns:
            tuple: (is_drowsy, is_yawning, is_head_slumped)
        """
        is_drowsy = False
        is_yawning = False
        is_head_slumped = False

        # Eye Logic
        if ear < self.ear_threshold:
            self.drowsiness_counter += 1
        else:
            self.drowsiness_counter = max(0, self.drowsiness_counter - 1)

        # Mouth Logic
        if mar > self.mar_threshold:
            self.yawn_counter += 1
        else:
            self.yawn_counter = max(0, self.yawn_counter - 1)
            
        # Pitch Logic (Head Slump)
        if pitch > self.pitch_threshold:
            self.pitch_counter += 1
        else:
            self.pitch_counter = max(0, self.pitch_counter - 1)

        if self.drowsiness_counter >= self.drowsiness_limit:
            is_drowsy = True
        
        if self.yawn_counter >= self.yawn_limit:
            is_yawning = True
            
        if self.pitch_counter >= self.drowsiness_limit:
            is_head_slumped = True

        return is_drowsy, is_yawning, is_head_slumped
