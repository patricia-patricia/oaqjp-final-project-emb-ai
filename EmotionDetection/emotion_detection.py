import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = { "raw_document": { "text": text_to_analyse } }, headers=header) 
    
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    
    result = emotions.copy()  # copy all scores
    result['dominant_emotion'] = max(emotions, key=emotions.get)
    
    return result

