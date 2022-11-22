from main import collection

person = {
    'first_name': 'Kira',
    'last_name': 'Erina',
    'Age': 3,
}

ins_result = collection.insert_one(person)
print(ins_result.inserted_id)
