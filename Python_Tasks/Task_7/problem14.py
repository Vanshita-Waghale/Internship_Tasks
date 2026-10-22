# Problem Name: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# Code:
def isValid(s):
    freq = Counter(s)
    count_freq = Counter(freq.values())

    if len(count_freq) == 1:
        return "YES"

    if len(count_freq) == 2:
        (f1, c1), (f2, c2) = count_freq.items()

        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"

        if (abs(f1 - f2) == 1) and (c1 == 1 or c2 == 1):
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
