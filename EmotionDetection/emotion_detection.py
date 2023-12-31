import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    emotionsSet = {}
    if response.status_code == 200:
        emotionsSet = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotionsSet, key=emotionsSet.get)
        emotionsSet['dominant_emotion'] = max_emotion
    elif response.status_code == 400:
        emotionsSet = { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }
    return emotionsSet