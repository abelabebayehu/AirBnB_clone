#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Dawit"
my_user.last_name = "Ethio"
my_user.email = "dave@airbnb.com"
my_user.password = "psssstiseedeadpeople"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "Hiwot"
my_user2.email = "hiwi@airbnb.com"
my_user2.password = "notlikeus"
my_user2.save()
print(my_user2)
