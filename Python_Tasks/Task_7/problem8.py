# Problem Name: Gemstones
# HackerRank Link: http://hackerrank.com/challenges/gem-stones/problem
# Code:
def gemstones(arr):
    # Write your code here
    common = set(arr[0])

    for stone in arr[1:]:
        common = common.intersection(set(stone))

    return len(common)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
