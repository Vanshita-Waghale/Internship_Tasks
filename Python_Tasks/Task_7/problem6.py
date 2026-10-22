# Problem Name: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem
# Code:
import math
import os
import random
import re
import sys

def pangrams(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    if alphabet.issubset(set(s.lower())):
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

