'''
TODO:
- Create the list to pull questions from (and descriptions for each)
- Add a manual post mode
- Add a way to manually enter the time between posts

'''

import json
import praw
import time




time.sleep(1)



with open('config.json') as data_file: #get file object and alias as data_file
        data = json.load(data_file) #load json data into a dict

test = data["data"]
print(test[1]) #outputs both key and value, want either/or

# These vars are loaded in from config.
clientID = data["clientID"] #Copy in data from JSON
secretKey = data["secretKey"] #Copy in data from JSON
userAgent = data["userAgent"] #Copy in data from JSON
myusername = data["username"] #Copy in data from JSON
mypassword = data["password"] #Copy in data from JSON

reddit = praw.Reddit(user_agent = userAgent, client_id = clientID, client_secret = secretKey,
                     username = myusername, password = mypassword)

# subreddits[3] = (reddit.subreddit('AskScience'), reddit.subreddit('nostupidquestions'), reddit.subreddit('questions'))
sub1 = reddit.subreddit('AskScience')
sub2 = reddit.subreddit('nostupidquestions')
sub3 = reddit.subreddit('questions')

# print(sub1.title)
# print(sub2.title)
# print(sub3.title)

# sub1.submit('Why are we the smartest creatures on this planet?', selftext = 'I\'ve only wondered this...Why did we get chosen to be the smartest?')
