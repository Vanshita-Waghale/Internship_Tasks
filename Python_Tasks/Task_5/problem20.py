# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem
# Code:
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))

    top = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()

        if pick > top:
            possible = False
            break

        top = pick

    print("Yes" if possible else "No")
