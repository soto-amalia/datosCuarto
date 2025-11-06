from datetime import datetime
from pymongo import MongoClient

mongo = MongoClient(host='localhost', port=27017)

datos = {
    'nombre': 'Isaac',
    'edad': 21,
    'intereses': ['Python', 'Ciencia de datos', 'Programar'],
    'fecha': datetime.now()
}

db = mongo.info #crea la base 'info'
coleccion = db.doc # crea coleccion 'doc'
print(coleccion.find_one()) #[]
print(db.list_collection_names())  #·['doc]

#debe de imprimir la coleccion vacia
coleccion.insert_one(datos)
db.list_collection_names()
#print(db.list_collection_names())
#es normal ver que pymongo no lo reconozca visual 