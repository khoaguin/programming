import pymongo
from pymongo import MongoClient

connection_str = "mongodb://localhost:27017/"
local = MongoClient("mongodb://localhost:27017/")

school_db = local.school

students = school_db.students
teachers = school_db.teachers


# for student in students.find():
#     print(student)

mike = {"name": "Mike", "age": 32, "subject": "Math"}
result = teachers.insert_one(mike)
print(result)
print(teachers.find_one({"name": "Mike"}))

# res = students.delete_one({"name": "Mike"})
# print(res)

# res = students.update_one({"name": "Spongebob"}, {"$set": {"age": 11}})
# print(students.find_one({"name": "Spongebob"}))

print(teachers.count_documents({}))
