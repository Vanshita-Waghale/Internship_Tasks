# Problem Name: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
# Code:
def gameOfThrones(s):
    # Write your code here
    freq = Counter(s)

    odd_count = 0

    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
