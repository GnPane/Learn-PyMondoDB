from main import collection

collection.update_one({'first_name': 'Irun'}, {'$set': {'Age': 56, 'first_name': 'Irina'}})

print(collection.find_one({'first_name': 'Irina'}).get('first_name'))
