import requests
import json

def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)
    response_dict = json.loads(response.text)
    status_code = response.status_code

    if text_to_analyze == "":
        score = ""
        label = ""
    elif status_code == 500: 
        score = None
        label = None
    else:
        score = response_dict["documentSentiment"]["score"]
        label = response_dict["documentSentiment"]["label"]

    dict = {
        "score": score,
        "label": label
    }
    
    return dict
