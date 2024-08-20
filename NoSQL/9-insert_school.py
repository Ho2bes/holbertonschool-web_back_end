#!/usr/bin/env python3
"""Script to insert into mongoDB"""


def insert_school(mongo_collection, **kwargs):
    """Method to insert into collection"""
    x = mongo_collection.insert_one(kwargs)

    return x.inserted_id
