from main import collection

person = {
    'first_name': 'Test',
    'last_name': 'Testov',
    'Age': 350,
}

ins_result = collection.insert_one(person)
print(ins_result.inserted_id)
