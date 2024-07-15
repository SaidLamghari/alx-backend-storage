#!/usr/bin/env python3
"""
Module to define a function that updates topics of a school
document based on name in a MongoDB collection.
Auteur SAID LAMGHRI
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics of a school document
    in MongoDB collection based on name.
    """
    # Update the document matching the name with new topics
    # Print a message indicating how many documents were modified (optional)
    mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })
