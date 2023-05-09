#!/usr/bin/env python3

"""
a python function that list all document in a collection
"""
import pymongo


def list_all(mongo_collection):
    all_doc = []
    for doc in mongo_collection.find():
        all_doc.append(doc)
    return (all_doc)
