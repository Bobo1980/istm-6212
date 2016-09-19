#!/usr/bin/env python

"""
A filter that converts words to lower cases.
"""

import fileinput

for line in fileinput.input():
    for word in line.split():
        print(word.lower())

    


