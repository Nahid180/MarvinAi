import json

with open('static/config.json','rb') as f:
    file=json.load(f)

file['Tag']='Greetings'

with open("static/config.json",'w') as writer:
    json.dump(file,writer,indent=2)


print(file['Tag'])