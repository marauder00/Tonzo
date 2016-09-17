import urllib2
import urllib
import sys
import base64
import json
import luis

# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# LUIS application URL 
luis_url = luis.Luis('https://api.projectoxford.ai/luis/v1/application?id=de15ad98-4809-4971-a30c-bb8470b6c78a&subscription-key=b0e5746863c04db4bb91e9a5583d2482')

# Your account key goes here. (used for cognitive services)
account_key = '37cf49dc60bb435db8706acf05894bba'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}


def determineCourseOfAction(input):
    if(classifyIntent(input)=="Greeting"):
        Greeting(input)
    elif(classifyIntent(input)=="Information"):
        Information(input) 
    elif(classifyIntent(input)=="Bye"):
        Bye(input)
    elif(classifyIntent(input)=="Emotion"):
        Emotion(input)
    elif(classifyIntent(input)=="Schedule"):
        Schedule(input)
    elif(classifyIntent(input)=="HowAreYou"):
        HowAreYou(input)
    elif(classifyIntent(input)=="Store"):
        Store(input)
    else:
        none(input)
        
def classifyIntent(input): 
    
    luisData = luis_url.analyze(input)
    return luisData.best_intent().intent #Return the intent
    
#Functions that deal with intents 
def Greeting(input):
    
    return "Hello"
    
def HowAreYou(input):
    
    return "Good"
    
def Schedule(input):

    return "Yes"
    
def Bye(input):
    
    return "Bye"
    
def Emotion(input):
    
    return "ok"
    
def Information(input):

    return "Ok"
    
def Store(input):

    return "OK"

def none(input):
    
    return "OK"
def Retrieve(type):

    return "OK"
def getMoodCheck(input):

    print "Mood Check"
def getInputText(input):
    return '{"documents":[{"id":"1","text":"' + input + '"}]}'
def getSentimentValue(input):
    batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
    batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
    input_texts = getInputText(input)
    req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
    response = urllib2.urlopen(req)
    result = response.read()
    obj = json.loads(result)
    for sentiment_analysis in obj['documents']:
        print('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score']))
        #return sentiment value
def getKeyPhrases(input):
    batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
    input_texts = getInputText(input)
    req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
    response = urllib2.urlopen(req)
    result = response.read()
    obj = json.loads(result)
    for keyphrase_analysis in obj['documents']:
        print('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases'])))
        #return key phrases

def main():

    
    
main()