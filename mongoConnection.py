from pymongo import MongoClient
client = MongoClient()

db = client.LIDLT
'''db.create_collection(name = 'Frases')
db.create_collection(name= 'Grupos')
db.create_collection(name= 'Participantes')'''

def insert_data (coll,data,database = db):
    res = database[coll].insert_one(data)
    return res.inserted_id

def read_data (query,coll,database = db, project=None):
    data= database[coll].find(query,project)
    return list(data)

def delete_data(coll,data,database = db):
    deleted = database[coll].remove(data)
    return f"You deleted {data} from {coll}"