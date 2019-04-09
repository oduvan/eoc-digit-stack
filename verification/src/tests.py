"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['PUSH 3', 'POP', 'POP', 'PUSH 4', 'PEEK', 'PUSH 9', 'PUSH 0', 'PEEK', 'POP', 'PUSH 1', 'PEEK'],
            "answer": 8
        },
        {
            "input": ['POP', 'POP'],
            "answer": 0
        },
        {
            "input": ['PUSH 9', 'PUSH 9', 'POP'],
            "answer": 9
        },
        {
            "input": [],
            "answer": 0
        },
    ],
    "Edge": [
        {
            "input": ['PUSH 0', 'PUSH 1', 'PUSH 2', 'PUSH 3', 'PUSH 4', 'PUSH 5', 'PUSH 6', 'PUSH 7', 'PUSH 8',
                      'PUSH 9'],
            "answer": 0
        },
        {
            "input": ['PEEK'],
            "answer": 0
        },
        {
            "input": ['POP'],
            "answer": 0
        },
        {
            "input": ['PUSH 0', 'PEEK', 'PUSH 1', 'PEEK', 'PUSH 2', 'PEEK', 'PUSH 3', 'PEEK', 'PUSH 4', 'PEEK',
                      'PUSH 5', 'PEEK', 'PUSH 6', 'PEEK', 'PUSH 7', 'PEEK', 'PUSH 8', 'PEEK', 'PUSH 9', 'PEEK'],
            "answer": 45
        }
        ],
    "Extra": [
        {
            "input": ['PUSH 3', 'PUSH 3', 'PUSH 0', 'POP', 'PEEK', 'PUSH 0', 'PUSH 2', 'PUSH 5', 'PUSH 1'],
            "answer": 3
        },
        {
            "input": ['PUSH 0', 'PUSH 5', 'POP', 'PUSH 9', 'PUSH 3', 'POP', 'PUSH 5', 'PUSH 6', 'PUSH 2', 'PUSH 7',
                      'POP', 'POP', 'PUSH 3', 'PUSH 0', 'PUSH 9', 'POP'],
            "answer": 26
        },
        {
            "input": ['POP', 'PUSH 1', 'POP', 'PUSH 8', 'PEEK', 'POP'],
            "answer": 17
        },
        {
            "input": ['POP', 'PUSH 6', 'PEEK', 'POP', 'POP', 'PUSH 1', 'POP', 'PUSH 3', 'POP', 'POP', 'POP', 'PEEK',
                      'PUSH 5', 'PEEK', 'PUSH 3', 'PEEK', 'PEEK', 'POP'],
            "answer": 30
        },
        {
            "input": ['PUSH 1', 'PEEK', 'PUSH 2', 'PUSH 1', 'PEEK', 'PUSH 1', 'PUSH 9', 'PEEK', 'PEEK', 'PUSH 8'],
            "answer": 20
        },
    ]
}
