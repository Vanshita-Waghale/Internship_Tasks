# Problem Name: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem
# Code:
def separateNumbers(s):
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        formed = ""

        while len(formed) < len(s):
            formed += str(current)
            current += 1

        if formed == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
