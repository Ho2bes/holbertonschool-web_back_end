#!/usr/bin/env python3
"""function that returns list of school"""


def schools_by_topic(mongo_collection, topic):
    """Method to return list of topics"""

    return mongo_collection.find({'topics': topic})
