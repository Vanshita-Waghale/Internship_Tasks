# Problem Name: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# Code:
def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    prev = ""

    for ch in s:
        value = ord(ch) - ord('a') + 1

        if ch == prev:
            current_weight += value
        else:
            current_weight = value

        weights.add(current_weight)
        prev = ch

    result = []
    
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
