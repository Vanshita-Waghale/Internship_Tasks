#Problem: Set .union() Operation
#HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem
#Code:

n = int(input())
english_students = set(map(int, input().split()))

b = int(input())
french_students = set(map(int, input().split()))

result = english_students.union(french_students)

print(len(result))
