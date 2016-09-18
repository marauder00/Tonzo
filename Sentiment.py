import urllib2
import urllib
import sys
import base64
import json
import luis
from random import randint

# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# LUIS application URL 
luis_url = luis.Luis('https://api.projectoxford.ai/luis/v1/application?id=de15ad98-4809-4971-a30c-bb8470b6c78a&subscription-key=b0e5746863c04db4bb91e9a5583d2482')

# Your account key goes here. (used for cognitive services)
account_key = '37cf49dc60bb435db8706acf05894bba'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}

emotionCount = 0

def firstTime(userId):
    #Determines whether or not it is the user's first time using the app
    #if()
    return True
    
def determineCourseOfAction(input, diaryEntry=True):
    if(emotionCount > 0):
        return Diary(input)
    elif(classifyIntent(input)=="Greeting"):
        return Greeting(input)
    elif(classifyIntent(input)=="Information"):
        return Information(input) 
    elif(classifyIntent(input)=="Bye"):
        return Bye(input)
    elif(classifyIntent(input)=="Emotion"):
        return Emotion(input, diaryEntry)
    elif(classifyIntent(input)=="Schedule"):
        return Schedule(input)
    elif(classifyIntent(input)=="HowAreYou"):
        return HowAreYou(input)
    elif(classifyIntent(input)=="Store"):
        return Store(input)
     #This means we have already recorded our diary entry
    else:
        return none(input)
        
def classifyIntent(input): 
    
    luisData = luis_url.analyze(input)
    return luisData.best_intent().intent #Return the intent
    
#Functions that deal with intents 
def Greeting(name):
    #If it is the user's first time using the application, give a brief explanation
    if(firstTime(name)==True):
        return "Hello! How are you feeling today?"
    else:
        return "Hello! My name is Tonzo." #todo extend this

def Diary(input):
    StoreSentiment(getSentimentValue(input)) #Store sentiment
    currentMood = getMoodCheck(input)
    Emotion(input)
    
def HowAreYou(input):
    randomChoice = randint(0,5)
    if(randomChoice == 1):
        return "I'm Good."
    elif(randomChoice ==2):
        return "I'm fine and dandy."
    elif(randomChoice == 3):
        return "I am fantastic."
    elif(randomChoice == 4):
        return "I'm well beyond describing!"
    elif(randomChoice == 5):
        return "I'm marvelous."
    
def Schedule(input):
    #Might be removed
    return "Yes"
    
def Bye(input):
    randomChoice = randint(0,4)
    if(randomChoice == 1):
        return "Bye Bye!"
    elif(randomChoice == 2):
        return "Talk to you later!"
    elif(randomChoice == 3):
        return "Bye!"
    elif(randomChoice == 4):
        return "Bye bye for now!"
        
    
def Emotion(input, askedAboutDay):
    if(askedAboutDay==False):
        return "Tell me about your day"
    else: 
        currentMood = getMoodCheck(input)
        if(currentMood=="Happy"):
            return Happy()
        elif(currentMood == "Stressed"): 
            return Stressed()
        elif(currentMood == "Sad"):
            return Sad(input)
        
        
def Sad(input):
    
    keyPhrases = getKeyPhrases(input).values()
    if('kill' in keyPhrases || 'death' in keyPhrases || 'dying' in keyPhrases):
        return Crisis()
    else:
        #Retrieve stuff->retrieve favourite things that belong to the person 
        randomChoice = randint(0,4)
        if(randomChoice == 1):
            return "Joke of some sort."
        elif(randomChoice == 2):
            return "Something else"
        elif(randomChoice == 3):
            return "Something else"
        elif(randomChoice == 4):
            return "Something else"

def Crisis():
    #We will hit the block if it is determined that the person is suicidal 
    #Steps
    #Suggest hotline->
    #Text friend->(use Twillio)
    
    
    return "Crisis"
def Stressed():
    randomChoice = randint(0,20)
    
    if(randomChoice == 1):
        return "Maybe try going for a walk?"
    elif(randomChoice ==2):
        return "Have you tried journaling?"
    elif(randomChoice ==3):
        return "How about you give guided meditation a try?"
    elif(randomChoice ==4):
        return "Treat yourself to a nice massage."
    elif(randomChoice == 5):
        return "How about you take a bubble bath!"
    elif(randomChoice == 6):
        return "Try exercising!"
    elif(randomChoice == 7):
        return "Listen to running water."
    elif(randomChoice == 8):
        return "Read a good book."
    elif(randomChoice == 9):
        return "Have you tried listening to some of your favourite music?"
    elif(randomChoice == 10):
        return "Maybe go on a lunch date with a good friend?"
    elif(randomChoice == 11):
        return "Take a nap. Remember that sleep is important."
    elif(randomChoice == 12):
        return "Have you tried going for a bike ride?"
    elif(randomChoice == 13):
        return "Maybe try doodling?"
    elif(randomChoice == 14):
        return "Try going for a walk on a beach."
    elif(randomChoice == 15):
        return "Have a dance party with some of your favourite songs!"
    elif(randomChoice == 16):
        return "Stretch and take some deep breaths!"
    elif(randomChoice == 17):
        return "You should treat yourself to your favourite meal."
    elif(randomChoice == 18):
        return "Watch some funny videos on youtube."
    elif(randomChoice == 19):
        return "Try curling up with your favourite hot beverage!"
    elif(randomChoice == 20):
        return "Try going to your local pet store"
    
    
def Happy():
    randomChoice = randint(0,5)
    value = "I'm glad that you are ok. "
    if(randomChoice==1):
        value += "Tell me what your favourite song is?"
    elif(randomChoice==2):
        value += "Tell me what your favourite movie is?"
    elif(randomChoice==3):
        value+= "Tell me what your favourite book is?"
    elif(randomChoice==4):
        value +=  "What kind of activites do you enjoy?"
    elif(randomChoice==5):
        value += "Who are you friends with?"  
    return value  
        
def Information(input):

    return "Ok"
    
def Store(input):

    return "OK"

def none(input):
    return "Sorry, I don't understand."
    
def Retrieve(type):

    return "OK"
def getMoodCheck(input):
    if(getSentiment(input) > 0.50):
        return "Happy"
    elif(getSentiment(input) > 0.12)
        return "Stressed"
    elif(getSentiment(input) < 0.12)
        return "Sad"
    
def StoreSentiment(input):
    print "Test"
    #Stores sentiment value in the database
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
        #print('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score']))
        return str(sentiment_analysis['score'])
def getKeyPhrases(input):
    batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
    input_texts = getInputText(input)
    req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
    response = urllib2.urlopen(req)
    result = response.read()
    obj = json.loads(result)
    for keyphrase_analysis in obj['documents']:
        return map(str,keyphrase_analysis['keyPhrases'])

def main():
    print determineCourseOfAction("I'm sad")
    print determineCourseOfAction("Oops")
    
    
main()