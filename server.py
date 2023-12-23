''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


#Initiate the flask app : TODO
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Function calling emotion detector."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    output = "For the given statement, the system response is "

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Iterate through the dictionary items
    for key, value in response.items():
        if key != "dominant_emotion":
            output += f"'{key}': {value}, "

    # Remove the trailing comma and space
    output = output[:-2]

    # Add the dominant emotion part
    output += f" and the dominant emotion is {response['dominant_emotion']}."
    return output


@app.route("/")
def render_index_page():
    """Function calling root route."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
