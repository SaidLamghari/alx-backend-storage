#!/usr/bin/env python3
"""
Module to define a function that
lists all documents in a MongoDB collection.
Auteur SAID LAMGHARI
"""
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> list:
    """
    List all documents in the given MongoDB collection.
    """
    dcumts = list(mongo_collection.find())
    return dcumts
