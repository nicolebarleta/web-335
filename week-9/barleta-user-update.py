"""
============================================
; Title:  Exercise 9.3 - Updating and Deleting Documents
; Author: Professor Krasso
; Date: 14 December 2020
; Modified By: Marie Nicole Barleta
; Description:  Updating documents
;===========================================

"""

#importing from pymongo and mongoclient

from pymongo import MongoClient

#importing pretty print
import pprint

#importing date time module
import datetime

#conneting to localhost mongodb
client = MongoClient('localhost', 27017)

#connecting to web335 database
db = client.web335
 

#update query on user's email 
db.users.update_one(

    {"employee_id": "0000002"},

    {

        "$set": {

            "email": "mnbarleta@my365.bellevue.edu"

        }

    }

)

#pretty print of employee_id with 0000002 and prints the details with user's email, employee_id, first_name, last_name

print("Updated email of user: ")
pprint.pprint(db.users.find_one({"employee_id": "0000002" } ,{"email": 1, "employee_id": 1, "first_name": 1, "last_name": 1} ))