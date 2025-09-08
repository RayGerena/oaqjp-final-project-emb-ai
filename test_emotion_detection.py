import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        emotions = emotion_detector("I am glad this happened")
        self.assertIn("dominant_emotion", emotions)
        self.assertEqual(emotions["dominant_emotion"], "joy")
        
    def test_anger(self):
        emotions = emotion_detector("I am really mad about this")
        self.assertIn("dominant_emotion", emotions)
        self.assertEqual(emotions["dominant_emotion"], "anger")
        
    def test_disgust(self):
        emotions = emotion_detector("I feel disgusted just hearing about this")
        self.assertIn("dominant_emotion", emotions)
        self.assertEqual(emotions["dominant_emotion"], "disgust")
        
    def test_sadness(self):
        emotions = emotion_detector("I am so sad about this")
        self.assertIn("dominant_emotion", emotions)
        self.assertEqual(emotions["dominant_emotion"], "sadness")
        
    def test_joyfear(self):
        emotions = emotion_detector("I am really afraid that this will happen")
        self.assertIn("dominant_emotion", emotions)
        self.assertEqual(emotions["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()
        