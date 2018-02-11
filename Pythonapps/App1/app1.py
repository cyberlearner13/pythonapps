import json
from difflib import get_close_matches as matches


data = json.load(open("data.json"))

def translate(wd):
    w = wd.lower()
    if w in data:
        return data[w]
    elif wd in data:
        return data[wd]
    elif len(matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes,N if no: " %matches(w,data.keys())[0])
        if yn == "Y":
            return data[matches(w,data.keys())[0]]
        elif yn == "N":
            return "Word does not exist.Please double check it"
        else:
            return "We did not understand your query" 
    else:
        return "Word does not exist.Please double check it"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)