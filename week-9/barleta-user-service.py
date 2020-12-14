"""
============================================
; Title:  Exercise 9.2 - Querying and Creating Documents
; Author: Professor Krasso
; Date: 14 December 2020
; Modified By: Marie Nicole Barleta
; Description:  Creating document example and findOne query
;===========================================

"""

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

#creating a new user to be inserted
newUser = {
    "first_name": "Alex",
    "last_name": "Arr",
    "email": "alexarr@ar.wow",
    "employee_id": "00000012",
    "date_created":datetime.datetime.utcnow()
}

#insert new user query
user_id = db.users.insert_one(newUser).inserted_id

#prints the auto_generated id from the inserted user
print("User: ",user_id ," Successfully added!") 


#prints a prompt that says details of found user
print("Details of found user: ") 
#findOne query to find the employee_id with 00000011, prints the found user
pprint.pprint(db.users.find_one({"employee_id": "00000011"}))