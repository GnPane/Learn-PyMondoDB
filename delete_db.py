from main import collection

collection.delete_many({'Age': {'$gt': 60}})

for person in collection.find().sort('Age', -1):
    print(person.get('first_name'))
