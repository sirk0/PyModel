"""
Test raising an exception, to check how clogdiff handles it
"""

cases = [
    ('Raise an exception - does traceback go to .log file?',
     'python -c "raise Exception"')
]
