from main import collection

collection.find_one_and_delete({'first_name': 'Ekaterina'})
# collection.delete_many({'Age': {'$gt': 60}})

for person in collection.find().sort('Age', -1):
    print(person.get('first_name'))
