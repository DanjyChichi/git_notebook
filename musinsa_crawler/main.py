import pymongo

client = pymongo.MongoClient("mongodb://3.37.184.54:27017")
collection = client.musinsa_db.musinsa_outer

demo_data = {
    'item_id': '12313',
    'item_price': 12312331,
    'item_title': "DEMO ITEM"
}

collection.insert_one(demo_data)