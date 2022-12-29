#!/usr/bin/python3
from models.base_model import BaseModel
from pprint import pprint

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print('\n')
my_model.save()
print(my_model)
print('\n')
my_model_json = my_model.to_dict()
pprint(my_model_json)
print('\n')
pprint("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))