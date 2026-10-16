# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem
# Code
if __name__ == '__main__':
    n = int(input()) 
    countries = set() 
    for _ in range(n): 
        country = input() 
        countries.add(country) 
    print(len(countries)) 
