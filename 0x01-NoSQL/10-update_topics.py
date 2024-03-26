#!/usr/bin/env python3
"""
NoSQL -Python
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    target = {"name": name}
    alter = {"$set": {"topics": topics}}
    mongo_collection.update_many(target, alter)
