#!/usr/bin/env python3

"""
a python function that list all document in a collection
"""


def list_all(mongo_collection):
    all_doc = mongo_collection.find():
        if all_doc.count() == 0:
            return []
    return all_doc
