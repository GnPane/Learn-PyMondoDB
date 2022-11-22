from main import collection

age = 36
name = ''

print(collection.find_one({'Age': age}))
print(collection.count_documents({'Age': age}))

for person in collection.find():
    print(person)

print()
print("Кол-во персон старше 18 лет")
print(collection.count_documents({'Age': {'$gt': 18}}))

print()
print("Кол-во персон младше 18 лет")
print(collection.count_documents({'Age': {'$lt': 18}}))

print()
print("Кол-во персон = 36 лет")
print(collection.count_documents({'Age': {'$eq': age}}))

print()
print("Кол-во персон = 36, 35, 34, 6 лет")
print(collection.count_documents({'Age': {'$in': (36, 35, 34, 6)}}))
