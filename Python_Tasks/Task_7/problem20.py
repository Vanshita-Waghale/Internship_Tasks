# Problem Name: Super Reduced String
# HackerRank Link: https://www.hackerrank.com/challenges/reduced-string/problem
# Code:
def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    result = "".join(stack)

    if result:
        return result
    else:
        return "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
