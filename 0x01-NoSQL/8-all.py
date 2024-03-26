#!/usr/bin/env python3
"""
NoSQL
"""

def list_all(mongo_collection):
    """
    Return all document in passed collection.
    """
    return mongo_collection.find()
