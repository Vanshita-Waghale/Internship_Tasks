# Problem Name: Making Anagrams
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem
# Code:
def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    deletions = 0

    for ch in set(s1 + s2):
        deletions += abs(count1[ch] - count2[ch])

    return deletions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
