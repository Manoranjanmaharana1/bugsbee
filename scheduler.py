import requests
from NewsClass import News
import asyncio
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import uuid
import time
import dateutil.parser

# Fetch the service account key JSON file contents
cred = credentials.Certificate('credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://technews-875b3-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')
async def printstatus(text):
    print(text)
    
async def callBingNews(cnt):
    url = "https://bing-news-search1.p.rapidapi.com/news"

    querystring = {"originalImg":"true","count":"100","mkt":cnt,"safeSearch":"Off","category":"ScienceAndTechnology","textFormat":"Raw"}

    headers = {
    'x-bingapis-sdk': "true",
    'x-rapidapi-key': "724182feffmsh7018ba2c6d8d107p16694bjsnfd0d94502637",
    'x-rapidapi-host': "bing-news-search1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    ls = {}

    for news in response.json()["value"]:
        if "image" in news.keys():
            date = (dateutil.parser.parse(news["datePublished"])).strftime("%d %B %Y %I:%M %p")
            newsObj = News(news["name"], news["description"], news["image"]["contentUrl"], date, news["url"], news["provider"][0]["name"])
            ob = json.dumps(newsObj.__dict__)
            data = json.loads(ob)
            ls[str(uuid.uuid1())] = data
    ref.push(ls)

async def callNewsCatcher(query):
    url = "https://newscatcher.p.rapidapi.com/v1/latest_headlines"

    querystring = {"topic":query,"lang":"en","media":"True"}

    headers = {
    'x-rapidapi-key': "724182feffmsh7018ba2c6d8d107p16694bjsnfd0d94502637",
    'x-rapidapi-host': "newscatcher.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    await printstatus(response.text)

async def callWebSearch(query):
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"

    querystring = {"q":query,"pageNumber":"1","pageSize":"10","autoCorrect":"true","safeSearch":"false","withThumbnails":"true","fromPublishedDate":"null","toPublishedDate":"null"}

    headers = {
    'x-rapidapi-key': "724182feffmsh7018ba2c6d8d107p16694bjsnfd0d94502637",
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    ls = {}
    for news in response.json()["value"]:
        newsObj = News(news["body"], news["body"], news["url"], news["datePublished"], news["url"], news["provider"]["name"])
        ob = json.dumps(newsObj.__dict__)
        data = json.loads(ob)
        ls[str(news["id"])] = data

    ref.push(ls)
    print("done")

async def main():
    while(True):
        print("hello")
        ref.set({})
        task1 = asyncio.create_task(callBingNews("en-US"))
        task2 = asyncio.create_task(callBingNews("en-GB"))
        task3 = asyncio.create_task(callBingNews("en-IN"))
        await asyncio.sleep(60)
asyncio.run(main())
