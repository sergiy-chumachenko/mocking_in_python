# Imagine we want to test this very simple function:

import os


def work_on():
    path = os.getcwd()
    print(f'Working on: {path}')
    return path


work_on()  # Working on: /home/user/Documents/Python/mocking_in_python
