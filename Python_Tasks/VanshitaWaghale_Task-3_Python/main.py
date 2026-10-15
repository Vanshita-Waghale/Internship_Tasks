# Answer Q1 
from solutions import word_frequency
print(word_frequency("python is easy and python is powerful."))
print(word_frequency("practices makes perfect and perfect is the key to success"))

# Answer Q2
from solutions import char_frequency
print(char_frequency("banana"))
print(char_frequency("frequency"))

# Answer Q3
from solutions import first_non_repeating_char
print(first_non_repeating_char("banana"))
print(first_non_repeating_char("Aarti"))

# Answer Q4
from solutions import are_anagrams  
print(are_anagrams("listen", "silent"))   #True
print(are_anagrams("hello", "world"))     # False

# Answer Q5
from solutions import first_repeating_char
print(first_repeating_char("programming"))  # 'r'
print(first_repeating_char("banana"))       # 'a'

# Answer Q6
from solutions import move_zeros_to_end  
print(move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))  # [3, 1, 2, 4, 0, 0, 0]
print(move_zeros_to_end([1, 0, 1, 2, 0, 1, 34, 0]))  # [1, 1, 2, 1, 34, 0, 0, 0]

# Answer Q7
from solutions import second_highest    
print(second_highest([10, 20, 40, 30, 40, 20]))  # 30
print(second_highest([5, 5, 5, 5]))        # None

# Answer Q8
from solutions import remove_duplicates
print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))  # [4, 2, 5, 7]
print(remove_duplicates([1, 2, 3, 2, 1, 4]))  # [1, 2, 3, 4]

# Answer Q9
from solutions import find_missing_number
print(find_missing_number([1, 2, 4, 5, 6], 6)) #3
print(find_missing_number([1, 2, 4, 6, 3, 7, 8], 8))  # 5

#Answer Q10
from solutions import find_two_numbers_with_sum
print(find_two_numbers_with_sum([2, 7, 11, 15], 9))  # (2, 7)
print(find_two_numbers_with_sum([1, 2, 3, 4, 5, 6, 7, 5], 8))  # (3, 5)

#Answer Q11
from solutions import find_closest_to_zero
print(find_closest_to_zero([-8, -3, 2, 5, -2]))  # 2
print(find_closest_to_zero([1, 2, 3, 4, 5]))  # 1

#Answer Q12
from solutions import find_common_elements
print(find_common_elements( [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # [3, 4, 5]
print(find_common_elements( [10, 20, 30], [40, 50, 60]))  # []

#Answer Q13
from solutions import rotate_list
print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(rotate_list([10, 20, 30, 40, 50], 3))  # [30, 40, 50, 10, 20]

#Answer Q14
from solutions import max_sum_of_consecutive_elements
print(max_sum_of_consecutive_elements([4, 7, 2, 9, 5])) # 14
print(max_sum_of_consecutive_elements([1, 2, 3, 4, 5]))  # 9

#Answer Q15
from solutions import find_all_pairs_with_sum
print(find_all_pairs_with_sum([2, 4, 3, 5, 7, 8, 1], 9))  # [[1, 8], [2, 7], [4, 5]]
print(find_all_pairs_with_sum([1, 2, 3, 4, 5], 5))  # [(1, 4), (2, 3)]