import pymongo
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.post

collection.insert_one({
    "tittle": "Bài Thơ"
    "author": "Hùng Biu"
    "content": "Thơ hay vch :D"
})
