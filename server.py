"""Flask server for emotion detection app."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """Handle emotion detection requests via GET."""
    statement = request.args.get('textToAnalyze', '')
    emotions = emotion_detector(statement)
    dominant_emotion = emotions["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
