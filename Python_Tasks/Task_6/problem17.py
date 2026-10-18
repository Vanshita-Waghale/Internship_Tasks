#Problem: Check Strict Superset
#HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
#Code:

a = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other_set = set(map(int, input().split()))

    if not a > other_set:
        result = False
        break

print(result)
