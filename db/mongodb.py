import pymongo

from env import mongo_uri

conn = pymongo.MongoClient(mongo_uri)
db = conn.golangGinBlog
col = db.aboutMe

def insert_log(log_data):
    try:
        res = col.insert_one(log_data)
    except Exception as e:
        print(e)

def find_log_by_sort(value):
    try:
        results = col.find({'sort': value})
        for log in results:
            return log['data']
    except Exception as e:
        print(e)

if __name__ == "__main__":
    res = find_log_by_sort("aboutMe")
    t = type(res)
    print(t)