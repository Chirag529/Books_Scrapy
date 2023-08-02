from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://Chirag59:yvoE4HGJXrlrwQdo@mongodbclustertesting.ks7p9rk.mongodb.net/")

db = client.scrapy

post = db.test_collection

doc = post = {
    "author": "Chirag",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

post_id = post.insert_one(doc).inserted_id