import json
import requests
import webbrowser
import io
#pip install requests

#Function for the normal defintion, gives the entire json response from google definitions
def NormalDef():
    print("Enter Word")
    def1 = input()
    api_url = 'https://mydictionaryapi.appspot.com'
    r = requests.get(url = api_url + "/?define=" + def1)
    j = r.json()
    print(j)
    print("Seach another word? y/n")
    researchN = input()
    if researchN == "y":
        NormalDef()
    else:
        exit()


def SubjectSeach():
    print("Search Word")
    sub_word = input()
    webbrowser.open('https://google.com/search?q=' + sub_word + "+" + sub_i)
    print("Seach another word? y/n")
    research = input()
    if research == "y":
        SubjectSeach()
    else:
        exit()

def SubjectInput():
    print("Enter Subject")
    global sub_i
    sub_i = input()
    print("Subject " + sub_i + " chosen")
    print("Search Word")
    sub_word = input()
    webbrowser.open('https://google.com/search?q=' + sub_word + "+" + sub_i)
    print("Seach another word? y/n")
    research = input()
    if research == "y":
        SubjectSeach()
    else:
        exit()

def batchImport():
    print("Batch importing definitions")
    print("make sure the definitions txt file has your definitions copied and pasted into it")
    timport = open("filename.txt","r")
    timport.read()


print("what type of definition search")
print("[1] Normal Definition")
print("[2] Subject Definition")
print("[3] Batch Import Definitions")
answer = input()
if answer == "1":
    NormalDef()
elif answer == "2":
    SubjectInput()
elif answer == "3":
    batchImport()
else:
    print("Invalid Input, Try Again")
