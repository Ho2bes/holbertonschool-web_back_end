#!/usr/bin/env python3
"""
nginx_stats.py
A script that provides statistics about Nginx logs stored in a MongoDB database.
"""

from pymongo import MongoClient


def nginx_log_stats():
    """Display stats about Nginx logs stored in MongoDB."""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_count = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")


if __name__ == "__main__":
    nginx_log_stats()
