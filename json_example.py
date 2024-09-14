import json

# 1. Convert Python dictionary to JSON string (Serialization)
person_dict = {
    "name": "Yash",
    "age": 21,
    "city": "Surat",
    "is_employee": True
}
person_json = json.dumps(person_dict, indent=4)
print("JSON String:")
print(person_json)

# 2. Convert JSON string 
# back to Python dictionary (Deserialization)
person_dict_back = json.loads(person_json)
print("\nBack to Python Dictionary:")
print(person_dict_back)

# 3. Write JSON data to a file
with open('person.json', 'w') as file:
    json.dump(person_dict, file, indent=4)
print("\nJSON data written to person.json")

# 4. Read JSON data from a file
with open('person.json', 'r') as file:
    person_from_file = json.load(file)
print("\nData read from person.json:")
print(person_from_file)
