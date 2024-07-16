#!/usr/bin/env python3
"""
Script to provide stats about
Nginx logs stored in MongoDB
Auteur SAIDLAMGHARI
"""
from pymongo import MongoClient


def log_stats():
    """
    Function to retrieve and display stat
    about Nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    ttl_logs = collection.count_documents({})
    print("{} logs".format(ttl_logs))

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        cnt = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, cnt))

    # Count logs with method=GET and path=/status
    cnt_status = collection.count_documents({"method": "GET",
                                             "path": "/status"})
    print("{} status check".format(cnt_status))
