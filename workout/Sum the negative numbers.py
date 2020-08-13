Write a Python program that removes the positive numbers from a given list of numbers. Sum the negative numbers and print the absolute value. Print the result.

Ans::

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]

print("Original list: ", nums)

print(abs(sum([i for i in nums if i < 0]))) 


O/P::

Original list:  [2, 4, -6, -9, 11, -12, 14, -5, 17]
32
