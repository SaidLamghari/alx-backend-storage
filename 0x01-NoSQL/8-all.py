#!/usr/bin/env python3
"""
Module to define a function that
lists all documents in a MongoDB collection.
Auteur SAID LAMGHARI
"""


def list_all(mongo_collection):
    """ Function"""
    return list(mongo_collection.find())
