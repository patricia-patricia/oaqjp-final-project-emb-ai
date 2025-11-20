from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    # Separate scores from dominant_emotion
    scores = {k: v for k, v in response.items() if k != 'dominant_emotion'}
    
    # Build the list like: 'anger': 0.006274985, 'disgust': 0.0025598293, ...
    scores_str = ", ".join(f"'{emotion}': {score}" for emotion, score in scores.items())
    
    dominant = response['dominant_emotion']

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {scores_str}. The dominant emotion is {dominant}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 

