# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem
# Code:
def merge_the_tools(string, k):
    for i in range(0, len(string),k):
        substring = string[i:i+k]
        result =""
        
        for ch in substring:
            if ch not in result:
                result += ch
                
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
