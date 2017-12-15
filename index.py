from bs4 import BeautifulSoup
from clarifai import rest
from clarifai.rest import ClarifaiApp
import requests
import json

app = ClarifaiApp(api_key='f7c8abc1ad6047f6a3a8e55749dce3dd');
model = app.models.get("general-v1.3")

def fillTweets(soup):
    for tweet in soup.findAll('div', {'class': 'tweet'}):
        tweetsIds.append(tweet['data-tweet-id'])
        tweets.append(tweet)

        for img in tweet.findAll('div', {'class': 'AdaptiveMediaOuterContainer'}):
            for i in img.findAll('img'):
                tweetsImgs.append(i['src'])

name = "emmanuelmacron"
url = "twitter.com/i/profiles/show/" + name + "/timeline/tweets/"

baseUrl = ""
r = requests.get("https://" + url)

jsonValue = json.loads(str(r.text))

soup = BeautifulSoup(jsonValue['items_html'], "html.parser")
tweetsIds = []
tweets = []
tweetsImgs = []

fillTweets(soup)

x = 0

while x <= 5:
    x += 1
    ur2 = "twitter.com/i/profiles/show/realDonaldTrump/timeline/tweets?include_available_features=1&include_entities=1&max_position=" + tweetsIds[-1] + "&reset_error_state=false"
    r = requests.get("https://" + ur2)

    jsonValue = json.loads(str(r.text))
    soup = BeautifulSoup(jsonValue['items_html'], "html.parser")
    fillTweets(soup)


#print(tweetsImgs)

for img in tweetsImgs:
    print(model.predict_by_url(url=img))