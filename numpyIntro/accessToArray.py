import numpy as np
#                                               rows columns
sample = np.random.uniform(0, 10, (3, 10))
print(f'Array\n{sample}\n')

print('1. Obtaining the 9th element from 2nd row using indexing')
print(sample[1, 8], '\n')

# if you want to get more than one element
print('2. Obtain the 8th and 9th element from 2nd row using indexing')
print(sample[1, [[7, 8]]], '\n')

print('3. Obtaining the 9th element from 2nd row using linear array\'s methods')
print(sample[1][8], '\n')

print('4. Obtain 2th element from the last')
print(sample[-2], '\n')

print('5. Obtain every 4th element from every row')
print(sample[:, 3], '\n')
# possible to arrange like in "for" system (e.g. : 2 => up to the second element not including)

# you can also use slices to get some elements from range with step
# by default step = 1, start = 0 end = array length on the indexing axis
print('6. Obtain elements from 2 row with  with range from 1 to 9 and step 3')
print(sample[1, 1:9:3], '\n')

print('7. Reversed array')
print(sample[::-1, ::-1], '\n')

# When you use a Boolean index array to index another array,
# elements matching True in the Boolean array will be selected
# and elements matching False will be ignored.
print('8. Boolean index array')
bool_array1 = np.random.choice([True, False], (3, 10))
print(bool_array1, '\n')
print(sample[bool_array1], '\n')
# If we change index array we change the main array
sample[bool_array1] = 11
print(sample, '\n')

# The logical operations logical_and, logical_or and
# logical_not are defined over indexing Boolean arrays
# will give an example with OR only (the rest are the same)
print('9. The logical operations')
bool_array2 = np.array([
    [False] * 10,
    [True, False, True, True, False] * 2,
    [True] * 10
])
print(bool_array2, '\n')
bool_array = np.logical_or(bool_array1, bool_array2)
print(bool_array, '\n')
print(sample[bool_array], '\n')

# Also we can use instead of logical_and, logical_or and logical_not &, | and ~ respectively
# and use as many operators as we want
print('10. The logical operations with special characters')
print(sample[bool_array1 | bool_array2])

# You can get an indexing logical array corresponding in form to the array of values
# by writing a logical condition with the array name as an operand
# * will be calculated as the truth of the expression for each element of the array
# ** it is worked out ONLY with commands (logical_and, logical_or or logical_not), but not with &, |, ~
print('11. The logical operations with each element of the array (Find elements which are more than 5 and less than 9)')
print(sample[np.logical_and(sample > 5, sample < 9)])
