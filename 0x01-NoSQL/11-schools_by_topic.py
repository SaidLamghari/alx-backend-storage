#!/usr/bin/env python3
"""
Module to define a function that returns a list
of schools having a specific topic in a MongoDB collection.
Auteur SAID LAMGHARI
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools from MongoDB collection that have a specific topic.
    """
    # Query MongoDB collection for schools with the given topic
    # Projection to include only 'name' and 'topics' fields
    schools = mongo_collection.find(
        {"topics": topic},
        {"name": 1, "topics": 1}
    )

    # Return list of schools matching the topic
    return list(schools)
