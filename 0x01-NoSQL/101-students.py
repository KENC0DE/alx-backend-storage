#!/usr/bin/env python3
"""
NoSQL -Python3
"""


def top_students(mongo_collection):
    """Get all students from the collection"""
    all_students = mongo_collection.find()

    students_with_avg = []
    for student in all_students:
        scores = student['scores']
        avg_score = sum(score['score'] for score in scores) / len(scores)
        student['averageScore'] = avg_score
        students_with_avg.append(student)

    sorted_students = sorted(students_with_avg,
                             key=lambda x: x['averageScore'], reverse=True)

    return sorted_students
