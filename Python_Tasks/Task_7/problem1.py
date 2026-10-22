# Problem Name: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Code:
n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.symmetric_difference(french)

print(len(result))
