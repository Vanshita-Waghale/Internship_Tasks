#Problem: Company Logo
#HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem
#Code:

from collections import Counter

s = input()

counter = Counter(s)

result = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

for char, count in result[:3]:
    print(char, count)
