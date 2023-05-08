#!/usr/bin/python3

"""
a Python function that inserts a new document
in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    new_doc = kwargs
    doc = mongo_collection.insert_one(new_doc)
    print(doc.inserted_id)
