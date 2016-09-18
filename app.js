var builder = require('botbuilder');

//Create bot and bind to console
var connector = new builder.ConsoleConnector().listen();
var bot = new builder.UniversalBot(connector);

//Create LUIS recognizer that points at our model and adds it as the root '/' dialog for our Bot
var model = "https://api.projectoxford.ai/luis/v1/application?id=de15ad98-4809-4971-a30c-bb8470b6c78a&subscription-key=b0e5746863c04db4bb91e9a5583d2482";
var recognizer = new builder.LuisRecognizer(model);
var dialog = new builder.IntentDialog({ recognizers: [recognizer]});
bot.dialog('/', dialog);

dialog.matches("Greeting", builder.DialogAction.send(Greeting());
dialog.matches("Bye", builder.DialogAction.send('Bye'));
dialog.matches("Store", builder.DialogAction.send('Store'));
dialog.matches("Information", builder.DialogAction.send('Information'));
dialog.matches("Emotion", builder.DialogAction.send('Emotion'));
dialog.onDefault(builder.DialogAction.send("I'm sorry I didnt' understand"));

function Greeting() { 


	return "Hello";


};

function Diary() { 



};

function HowAreYou() { 



};

function Schedule() { 
	//Feature might be removed 

}; 

function Bye() { 



};

function Emotion() { 



}; 


function Sad() { 


};

function Crisis() { 



}; 



function Stressed() { 

};


function Happy() { 



}; 


function Information() { 


};


function Store() { 

	//Storing data in Danyal's Database

};

function Retrieve() { 
	//Retreiving data from the database


}; 

function getMoodCheck() { 



};


function StoreSentiment() { 



};


function getSentimentValue() { 



}; 


function getKeyPhrases() { 


}; 



