#Tonzo Sentiment and Key Phrases
import urllib2
import urllib
import sys
import base64
import json

#Use LUIS to recognize intents 
# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# Your account key goes here.
account_key = '37cf49dc60bb435db8706acf05894bba'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}


def determineCourseOfAction(input):
    if(classifyIntent(input)=="greeting"): #Might have to use LUIS for this
        return "Greeting" #Jump to function to do things->Set a flag which we will keep globally
def classifyIntent(input):
    #UseKeyphrases for this maybe
    #Can we use luis
    #Greetings
    #HowAreYou
    #Making an Appointment
    #Happy->Information gathering mood
    #Sad
    #Crisis
    #Information of Mental Health Illnesses-Leave this to last
    #Mental health institutions in the area
    #Goodbye
    print "classify Intent"
def getMoodCheck(input):
    #This function will basically track the person's mood->we will do mood checks every once in a
    #while
    
    #ToDo store this data in a database 
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
    getSentimentValue("Tonzo is my little baby and makes me happy")
    getKeyPhrases("Hack the North")
    
    
main()