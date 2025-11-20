"""
Flask application for Emotion Detection.
Provides a web interface and API endpoint to analyze text emotion using Watson NLP.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")


@app.route("/emotionDetector")
def sent_analyzer() -> str:
    """
    Analyze the emotion of the text provided via the 'textToAnalyze' query parameter.
    Returns a formatted string with emotion scores and dominant emotion.
    If input is invalid or analysis fails, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    # Extract scores excluding dominant_emotion
    scores = {
        emotion: score
        for emotion, score in response.items()
        if emotion != "dominant_emotion"
    }

    # Format: 'anger': 0.123, 'joy': 0.456, ...
    scores_str = ", ".join(f"'{emotion}': {score}" for emotion, score in scores.items())
    dominant = response["dominant_emotion"]

    return (
        f"For the given statement, the system response is {scores_str}. "
        f"The dominant emotion is {dominant}."
    )


@app.route("/")
def render_index_page() -> str:
    """Render the main page with the input form."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
