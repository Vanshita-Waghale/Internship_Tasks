#Problem: Set .intersection() Operation
#HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
#Code:

n = int(input())
english_students = set(map(int, input().split()))

b = int(input())
french_students = set(map(int, input().split()))

result = english_students.intersection(french_students)

print(len(result))
