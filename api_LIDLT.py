from flask import Flask,request

# Import from the mongoConnection file my generic functions
from mongoConnection import read_data
from mongoConnection import insert_data

from bson import json_util, ObjectId


app = Flask("LIDLT")

@app.route("/inicio")
def inicio():
    return "Si no conoces el reality La Isla de las tentaciones visita:  https://www.telecinco.es/la-isla-de-las-tentaciones/"

# "Get" endpoints

@app.route("/mensajes")
def mensajes(): 
    data = read_data({},"Frases", project = {"_id":0,"Mensaje":1})
    return json_util.dumps(data)

@app.route("/participantes")
def participantes(): 
    data = read_data({},"Participantes", project = {"_id":0,"Nombre":1})
    return json_util.dumps(data)

@app.route("/participantes/details/<participante_id>")
def participantes_details(participante_id):
    try: #hacemos un try/exept para prevenir fallos si se introduce un "participante_id" que no sea un ObjectId
        id_ = ObjectId(participante_id) 
    except: 
        return {"Error": "participante_id no válido"},400
       
    q = {"_id": id_}
    data = read_data (q,"Participantes")
    if len(data) == 0:
        return{"error":"No hay ningun participante con ese id"}
    return json_util.dumps(data)

# "Post"  endpoints

@app.route("/participantes/new")
def participantes_new():
    args = dict(request.args)
    q = {"Nombre":args["Nombre"]}
    data = read_data(q, coll = "Participantes")
    if len(data)>0:
        return {"Error":"El participante ya existe"}
    res = insert_data (coll = "Participantes", data = args)
    return json_util.dumps({"_id":res})

app.run(debug = True)