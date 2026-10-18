#Problem: Set .difference() Operation
#HackerRank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
#Code:

n = int(input())
english_students = set(map(int, input().split()))

b = int(input())
french_students = set(map(int, input().split()))

result = english_students.difference(french_students)

print(len(result))
