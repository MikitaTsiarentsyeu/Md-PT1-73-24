import json
import pickle

with open("data.txt", 'r') as f:
    cars_data = eval(f.read())

print(json.dumps(cars_data))

with open("test.json", 'w') as f:
    json.dump(cars_data, f)

with open("test.json", 'r') as f:
    new_cars_data = json.load(f)

print(new_cars_data)
print(new_cars_data == cars_data)

with open("test.pickle", 'wb') as f:
    pickle.dump(cars_data, f)

with open("test.pickle", 'rb') as f:
    new_cars_data = pickle.load(f)

print(new_cars_data)
print(new_cars_data == cars_data)
