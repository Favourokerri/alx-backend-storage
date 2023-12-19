#!/usr/bin/env python3
"""
    a Python function that lists all
    documents in a collection
"""


def list_all(mongo_collection):
    """ list all documents """
    if mongo_collection is None:
        return []
    else:
        cursor = mongo_collection.find()
        document = [doc for doc in cursor]
        return document
