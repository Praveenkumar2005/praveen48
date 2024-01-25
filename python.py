# Question 1: Calculate the sum of all numbers from 1 to n.
def sum_of_numbers(n):
    return n * (n + 1) // 2

# Question 2: Reverse a given list.
def reverse_list(lst):
    return lst[::-1]

# Question 3: Check if a number is prime.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Question 4: Find the square root of a number.
def square_root(num):
    return num**0.5

# Question 5: Count the occurrences of each element in a list.
def count_occurrences(lst):
    from collections import Counter
    return Counter(lst)

# Question 6: Check if a string is an anagram of another string.
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Question 7: Implement a stack using a list.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

# Question 8: Calculate the factorial of a given number using recursion.
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Question 9: Remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

# Question 10: Check if a given year is a leap year.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Question 11: Find the maximum element in a list.
def find_max(lst):
    return max(lst)

# Question 12: Merge two sorted lists into a single sorted list.
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# Question 13: Check if a string is a valid palindrome.
def is_valid_palindrome(s):
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

# Question 14: Swap two variables without using a temporary variable.
def swap_variables(a, b):
    a, b = b, a
    return a, b

# Question 15: Find the common elements between two lists.
def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Question 16: Implement a queue using two stacks.
class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()

# Question 17: Generate the nth Fibonacci number.
def fibonacci_nth(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Question 18: Find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Question 19: Implement a binary search algorithm.
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Question 20: Calculate the average of numbers in a list.
def calculate_average(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0

# Question 21: Convert a decimal number to binary.
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Question 22: Implement a simple calculator.
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else 'Cannot divide by zero'
    else:
        return 'Invalid operator'

# Question 23: Check if a list is sorted in ascending order.
def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Question 24: Find the longest common prefix of a list of strings.
def longest_common_prefix(strings):
    if not strings:
        return ''
    prefix = strings[0]
    for string in strings[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        prefix = prefix[:i]
    return prefix

# Question 25: Rotate a list to the right by k steps.
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

# Testing the solutions

# Question 1
print("Question 1 - Sum of numbers from 1 to 5:", sum_of_numbers(5))

# Question 2
print("Question 2 - Reverse [1, 2, 3, 4, 5]:", reverse_list([1, 2, 3, 4, 5]))

# Question 3
print("Question 3 - Is 11 a prime number?", is_prime(11))

# Question 4
print("Question 4 - Square root of 16:", square_root(16))

# Question 5
print("Question 5 - Occurrences in [1, 2, 2, 3, 3, 3]:", count_occurrences([1, 2, 2, 3, 3, 3]))

# Question 6
print("Question 6 - Is 'listen' an anagram of 'silent'?", is_anagram('listen', 'silent'))

# Question 7
print("Question 7 - Implementing a Stack:")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Pop from stack:", stack.pop())
print("Is stack empty?", stack.is_empty())

# Question 8
print("Question 8 - Recursive factorial of 4:", factorial_recursive(4))

# Question 9
print("Question 9 - Remove duplicates from [1, 2, 2, 3, 4, 4]:", remove_duplicates([1, 2, 2, 3, 4, 4]))

# Question 10
print("Question 10 - Is 2024 a leap year?", is_leap_year(2024))

# Question 11
print("Question 11 - Find the max in [5, 12, 8, 3, 9]:", find_max([5, 12, 8, 3, 9]))

# Question 12
print("Question 12 - Merge sorted lists [1, 3, 5] and [2, 4, 6]:", merge_sorted_lists([1, 3, 5], [2, 4, 6]))

# Question 13
print("Question 13 - Is 'A man, a plan, a canal, Panama!' a valid palindrome?", is_valid_palindrome("A man, a plan, a canal, Panama!"))

# Question 14
print("Question 14 - Swap variables 5 and 10:", swap_variables(5, 10))

# Question 15
print("Question 15 - Common elements in [1, 2, 3] and [2, 3, 4]:", find_common_elements([1, 2, 3], [2, 3, 4]))

# Question 16
print("Question 16 - Implementing a Queue with Two Stacks:")
queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeue from queue:", queue.dequeue())

# Question 17
print("Question 17 - 8th Fibonacci number:", fibonacci_nth(8))

# Question 18
print("Question 18 - GCD of 24 and 36:", gcd(24, 36))

# Question 19
print("Question 19 - Binary search in [1, 2, 3, 4, 5] for target 3:", binary_search([1, 2, 3, 4, 5], 3))

# Question 20
print("Question 20 - Average of [2, 4, 6, 8, 10]:", calculate_average([2, 4, 6, 8, 10]))

# Question 21
print("Question 21 - Binary representation of 10:", decimal_to_binary(10))

# Question 22
print("Question 22 - Calculator: 5 + 3 =", calculator(5, 3, '+'))

# Question 23
print("Question 23 - Is [1, 2, 3, 4] sorted in ascending order?", is_sorted_ascending([1, 2, 3, 4]))

# Question 24
print("Question 24 - Longest common prefix of ['apple', 'apricot', 'app']:",
      longest_common_prefix(['apple', 'apricot', 'app']))

# Question 25
print("Question 25 - Rotate [1, 2, 3, 4, 5] to the right by 2 steps:", rotate_list([1, 2, 3, 4, 5], 2))
