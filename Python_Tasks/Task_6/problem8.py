# Problem: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem
# Code:
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print hash(integer_list)
# This code will only run in python 2 because of hash algorithm.
