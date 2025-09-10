from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Home route serving index.html
@app.route('/')
def home():
	return render_template('index.html')


# Emotion detection route supporting GET requests
@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
	statement = request.args.get('textToAnalyze', '')
	emotions = emotion_detector(statement)
	dominant_emotion = emotions["dominant_emotion"]
	response = (
		f"For the given statement, the system response is 'anger': {emotions['anger']}, "
		f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
		f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
		f"The dominant emotion is {dominant_emotion}."
	)
	return response

if __name__ == '__main__':
	app.run(debug=True)