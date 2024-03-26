#!/usr/bin/env python3
"""
NoSQL -Python
"""
if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    coll = db['nginx']

    total_count = coll.count_documents({})
    get_count = coll.count_documents({"method": "GET"})
    post_count = coll.count_documents({"method": "POST"})
    put_count = coll.count_documents({"method": "PUT"})
    patch_count = coll.count_documents({"method": "PATCH"})
    delete_count = coll.count_documents({"method": "DELETE"})
    get_status = coll.count_documents({"method": "GET", "path": "/status"})

    message = f"""{total_count} logs
    Methods:
        method GET: {get_count}
        method POST: {post_count}
        method PUT: {put_count}
        method PATCH: {patch_count}
        method DELETE: {delete_count}
    {get_status} status check"""

    print(message)
