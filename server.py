"""Flask application for emotion detection."""
from flask import Flask, render_template,request
from EmotionDetection.emotion_detection import emotion_detector
app=Flask(__name__)
@app.route("/emotionDetector")
def emotion_detection():
    """Detect emotions in the given text and return formatted response."""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}.")
@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
