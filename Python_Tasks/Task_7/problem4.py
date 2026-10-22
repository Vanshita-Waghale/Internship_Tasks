# Problem Name: Funny String
# HackerRank Link: https://www.hackerrank.com/challenges/funny-string/problem
# Code: 
import os

def funnyString(s):
    for i in range(1, len(s)):
        left = abs(ord(s[i]) - ord(s[i - 1]))
        right = abs(ord(s[-i]) - ord(s[-i - 1]))

        if left != right:
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
