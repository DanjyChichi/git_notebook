from flask import Flask, render_template, jsonify
import pymongo

client = pymongo.MongoClient("mongodb://3.37.184.54:27017")
collection = client.musinsa_db.musinsa_outer

app = Flask(__name__)

@app.route("/musinsa_search")
def musinsa_search_page():
    return render_template("musinsa_search.html")

# 주 임무는 여기!
@app.route("/api/musinsa_search/<price>")
def musinsa_search_price(price):
    # 조건 문서 - criteria
    criteria = {
        'item_price': {"$lte": int(price)}
    }

    datas = collection.find(criteria, {"_id": False})

    return jsonify(list(datas))

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)