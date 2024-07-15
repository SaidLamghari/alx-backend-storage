#!/usr/bin/env python3
"""
Module to define a function that inserts a
document in a MongoDB collection based on kwargs.
Auteur SAID LAMGHARI
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the MongoDB
    collection with the provided kwargs.
    Return the _id of the newly inserted document.
    """
    # Insert a new document with the provided kwargs
    rslt = mongo_collection.insert_one(kwargs)

    # Return the _id of the newly inserted document
    return str(rslt.inserted_id)
