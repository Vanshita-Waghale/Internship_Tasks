# collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
# Code:
from collections import Counter

X = int(input())
shoes = list(map(int, input().split()))
N = int(input())

stock = Counter(shoes)
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())

    if stock[size] > 0:
        earnings += price
        stock[size] -= 1

print(earnings)
