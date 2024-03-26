#!/usr/bin/env python3
"""
NoSQL -Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collectin based on @kwargs
    """
    return mongo_collection.insert_one(kwargs).inserted_id
