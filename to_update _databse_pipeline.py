import json

from pymongo import MongoClient
from pathlib import Path
client = MongoClient('localhost', 27017)
db = client.ganeshdb

collection = db.news_dataset

old_link=[]
c=0
for i in collection.find():
    old_link.append(i['url'])

print("existing total number of records in database are",len(old_link))

windows_path=r"/home/sets/PycharmProjects/news_crawling/alt_news/10_05.json"
json_file=Path(windows_path)
with open(json_file, "r",encoding="utf8") as f:
    new_data = json.load(f)
    for i in new_data:
        if i['url'] not in old_link:
            collection.insert_one(i)
            c+=1
print("no. of record added today in database",c)