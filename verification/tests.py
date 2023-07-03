"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[0, 0]],
            "answer": 2,
            "explanation": [0, 1],
        },
        {
            "input": [[2, 3, 3, 2]],
            "answer": 1,
            "explanation": [1],
        },
        {
            "input": [[1, 0, 1, 0]],
            "answer": 2,
            "explanation": [0, 2],
        },
    ],
    "Extra": [
        {
            "input": [[0, 0, 0, 1, 2, 0, 2, 0, 0]],
            "answer": 4,
            "explanation": [0, 1, 4, 6],
        },
        {
            "input": [[0, 0, 2, 3, 4, 1, 0, 1, 2, 2, 5, 2, 3, 0, 1, 0, 0]],
            "answer": 3,
            "explanation": [4, 10, 16],
        },
        {
            "input": [[0, 2, 2, 2, 2, 0, 1, 2, 0, 0, 1, 1, 1, 0, 1, 0, 0, 
2, 1, 1, 0, 1, 1, 2, 0, 0, 1]],
            "answer": 8,
            "explanation": [2, 7, 11, 14, 17, 19, 23, 26],
        },
    ]
}
