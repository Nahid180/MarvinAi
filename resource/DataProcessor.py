import nltk
import json

with open('Brain\Memory\TrainData.json') as f:
    data=json.load(f)

all_words=[]
x=[]
y=[]

for i in data['intents']:
    for word in i['pattern']:
        tokenize=nltk.tokenize
        print(word.lower())