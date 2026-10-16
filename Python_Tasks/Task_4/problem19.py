# collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
# Code
from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoe_sizes = Counter(map(int, input().split()))

    n = int(input())
    earnings = 0

    for _ in range(n):
        size, price = map(int, input().split())

        if shoe_sizes[size] > 0:
            earnings += price
            shoe_sizes[size] -= 1

    print(earnings)
