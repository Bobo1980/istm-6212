#!/usr/bin/env python

"""
A filter that splits lines of text into lines of words while removing all punctuations.
"""

import fileinput
import re

for line in fileinput.input():
    for word in re.findall(r'\w{2,}', line):
        """re.findall separates the words while stripping punctuations"""
        print(word)



