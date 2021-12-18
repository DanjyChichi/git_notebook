import pymongo

# Pipeline클래스는 객체가 1개만 만들어 진다.
class MusinsaCrawlerPipeline:

    def __init__(self):
        client = pymongo.MongoClient("mongodb://3.37.184.54:27017")
        # collection 객체는 한개만 있으면 된다.
        self.collection = client.musinsa_db.musinsa_outer

    def __insert_document__(self, item):
        # 매번 데이터를 insert 하기 위해 collection 객체를 만들 필요는 없다.
        item_id = item['item_id']
        item_title = item['item_title']
        item_price = item['item_price']

        doc = {
            'item_id': item_id,
            'item_title': item_title,
            'item_price': item_price
        }

        # pipeline 클래스가 만들어 질 때 같이 만들어진 collection 객체를 사용하면 된다.
        self.collection.insert_one(doc)

    def process_item(self, item, spider):

        print("="*50)
        print(item)
        print("=" * 50)

        self.__insert_document__(item)
        return item
