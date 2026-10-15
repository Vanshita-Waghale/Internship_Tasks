#Q1 Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    word_count={}
    words=sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

#Q2 Find the Frequency of Each Character in a String
def char_frequency(string):
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

#Q3 Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
    char_count={}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1    
            
    for char in word:
        if char_count[char] == 1:
            return char
    return None

#Q4 Check Whether Two Strings Are Anagrams
#def are_anagrams(str1, str2):
   # return sorted(str1) == sorted(str2)
#lower() converts all letters to lowercase, so 'A' and 'a' are treated as the same character before comparison.
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

#Q5. Find the First Repeating Character in a String
def first_repeating_char(string):
    char_count={}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1    
            
    for char in string:
        if char_count[char] > 1:
            return char
    return None

# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(lst):
    non_zero_elements = [x for x in lst if x != 0]
    zero_count = lst.count(0)
    return non_zero_elements + [0] * zero_count

#Q7. Find the Second Highest Distinct Number in a List
def second_highest(lst):
    distinct_numbers = list(set(lst))
    if len(distinct_numbers) < 2:
        return None
    distinct_numbers.sort(reverse=True)
    return distinct_numbers[1]

#Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

#Q9. Find the Missing Number from 1 to N
def find_missing_number(lst, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

#Q10. Find Two Numbers Whose Sum Equals a Target
def find_two_numbers_with_sum(lst, target):
    num_set = set()
    for num in lst:
        complement = target - num
        if complement in num_set:
            return (complement, num)
        num_set.add(num)
    return None

# Q11. Find the Number Closest to Zero
def find_closest_to_zero(lst):
    closest = None
    for num in lst:
        if closest is None or abs(num) < abs(closest):
            closest = num
    return closest

# Q12. Find Common Elements Between Two Lists
def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

#Q13. Rotate a List to the Right by K Positions
def rotate_list(lst, k):
    k = k % len(lst)  # Handle cases where k is greater than the length of the list
    return lst[-k:] + lst[:-k]

#Q14. Find the Maximum Sum of Two Consecutive Elements
def max_sum_of_consecutive_elements(lst):
    if len(lst) < 2:
        return None
    max_sum = lst[0] + lst[1]
    for i in range(1, len(lst) - 1):
        current_sum = lst[i] + lst[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def find_all_pairs_with_sum(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs
