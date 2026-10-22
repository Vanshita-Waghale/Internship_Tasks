# Problem Name: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem
# Code:
import math
import os
import random
import re
import sys

def marsExploration(s):
    changed = 0

    for i in range(len(s)):
        expected = "SOS"[i % 3]

        if s[i] != expected:
            changed += 1

    return changed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
