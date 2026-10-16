# Find the Runner-Up Score 
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Code
n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)

    while max_score in arr:
        arr.remove(max_score)

    print(max(arr))
