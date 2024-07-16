#!/usr/bin/env python3
"""
Python script to fetch and display statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def get_nginx_stats():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017')
        # Select the collection 'nginx' in the database 'logs'
        nginx_collection = client.logs.nginx

        # Count total logs
        total_logs = nginx_collection.count_documents({})
        print(f"{total_logs} logs")

        # Count by HTTP method
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            method_count = nginx_collection.count_documents({"method": method})
            print(f"\tmethod {method}: {method_count}")

        # Count status checks (GET /status)
        status_check_count = nginx_collection.count_documents({
            "method": "GET",
            "path": "/status"
        })
        print(f"{status_check_count} status check")

    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if client:
            client.close()


if __name__ == "__main__":
    get_nginx_stats()
