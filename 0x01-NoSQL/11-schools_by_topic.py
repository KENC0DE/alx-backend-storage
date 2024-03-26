#!/usr/bin/env python3
"""
NoSQL -Python
"""


def schools_by_topic(mongoc, topic):
    """
    Find schools having specific topic
    """
    return list(mongoc.find({"topic": topic}))
