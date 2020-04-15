import json
filename = 'json.txt'
lst = []

def tweet(filename, tweets):
    lst.append ({'text':tweet})
    with open (filename, 'w') as fileobject:
        json.dump({"statuses": lst}, fileobject)
        
while True :
    print("1. List all my tweets \n 2. Tweet")
    
    try:
        select = int(input ("Select 1/2 options: "))
        if select == 1 :
            with open (filename) as fileobject:
                content = json.load(fileobject)
                lst = content['statuses']
                print ("Here are the tweets you have tweeted: ")
                for i in range(len(lst)):
                    i = i + 1
                    print(lst[i]["text"])
                print('')
        elif select == 2:
            tweet_string= str(input("Enter your tweet: "))
            tweet(filename, tweets)