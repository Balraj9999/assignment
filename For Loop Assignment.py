#!/usr/bin/env python
# coding: utf-8

# # Basic Level

# In[1]:


#1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.
r=range(1,11)
for i in r:
    print(i)


# In[7]:


#2. Create a program that calculates the sum of all numbers in a list using a `for` loop.
l=[1,2,3,4,5]
def sum(l):
    s=0
    for i in l:
        s=s+i
    return s
        


# In[8]:


sum(l)


# In[12]:


#3.Write a program to print the characters of a string in reverse order using a `for` loop.
s='pwskills'
def r_s(s):
    k=''
    for i in range(len(s)-1,-1,-1):
        k=k+s[i]
    return k
    


# In[13]:


r_s(s)


# In[20]:


#4. Develop a program that finds the factorial of a given number using a `for` loop.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage:
number = int(input("Enter a number: "))
factorial_result = factorial(number)
print("Factorial of", number, "is:", factorial_result)


# In[21]:


#5. Create a program to print the multiplication table of a given number using a `for` loop.
n=int(input('enter the table you want'))
for i in range(1,11):
    print('{}*{}={}'.format(n,i,n*i))


# In[31]:


#6. Write a program that counts the number of even and odd numbers in a list using a `for` loop.
l=[1,2,3,4,5]
e_n=0
o_n=0
for i in l:
    if i%2==0:
        e_n=e_n+1
    elif i%2==1:
        o_n=o_n+1
    else:
        print('hello')
print("even_no count={}".format(e_n))
print("odd_no count={}".format(o_n))
     


# In[32]:


#7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.
a=range(1,6)
for i in a:
    i=i**2
    print(i)
    


# In[36]:


#8.Create a program to find the length of a string without using the `len()` function.
s1='hello'
count=0
for i in s1:
    if type(i)==str:
        count=count+1
print("the len of s1 is",count)


# In[47]:


#9Write a program that calculates the average of a list of numbers using a `for` loop.
l3=[1,2,3,4,5]
avg=0
for i in l3:
    if type(i)==int or type(i)==float:
        avg=avg+i/len(l3)
print(avg)


# In[50]:


#10.Develop a program that prints the first `n` Fibonacci numbers using a `for` loop.
def fib(num):
    a=0
    b=1
    for i in range(num):
        yield a
        a,b=b,a+b


# In[53]:


for i in fib(5):
    print(i)


# # Intermediate Level:

# In[12]:


#11. Write a program to check if a given list contains any duplicates using a `for` loop.
l5=[1,1,1,2,3,4,4,4]
d=[]
n_u=[]
for i in l5:
    if i in n_u:
        d.append(i)
    else:
        n_u.append(i)
print(d,n_u)


# In[20]:


#12. Create a program that prints the prime numbers in a given range using a `for` loop.
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
 #function to print prime numbers with in a given range
def print_prime(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            print(num)
start_num=int(input("enter a number"))
end_num=int(input("enter a number"))
print_prime(start_num,end_num)


# In[34]:


#13. Develop a program that counts the number of vowels in a string using a `for` loop.
a='hello'
v='aeiou'
c=0
for j in v:
    for i in a:
        if i==j:
            c=c+1
            print(i)
print('count=',c)


# In[35]:


#14. Write a program to find the maximum element in a 2D list using a nested `for` loop.
l6=[[1,2,3],[4,5,6]]
m_e=0
for i in l6:
    for j in i:
        if j>m_e:
            m_e=j
print("the maximum element is",m_e)
    


# In[42]:


#15. Create a program that removes all occurrences of a specific element from a list using a `for` loop.
l7=[1,1,1,2,3,4,4]
e_to_remove=int(input('enter the element present in list to remove'))
n_l=[]
for i in l7:
    if i!=e_to_remove:
        n_l.append(i)
print('the new list is',n_l)


# In[48]:


#16. Develop a program that generates a multiplication table for numbers from 1 to 5 using a nested `for` loop.
# Initialize the list for the multiplication table
t = [[] for _ in range(5)]

# Generate the multiplication table
for i in range(1, 6):  # Numbers from 1 to 5
    for j in range(1, 11):  # Multiplication from 1 to 10
        t[i - 1].append(i * j)

# Print the multiplication table
for row in t:
    for element in row:
        print(element, end='\t')
    print()  # Move to the next row


# In[51]:


#17. Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.
t_c=[21,43,54,76]
for i in t_c:
    print((9/5)*i+32)
    


# In[52]:


#18. Create a program to print the common elements from two lists using a `for` loop.
t_l=[1,2,3,4,5]
t_2=[1,2,3,7,8]
for i in t_l:
    for j in t_2:
        if i==j:
            print(i)


# In[55]:


#19. Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the
#pattern
a=int(input("enter the number"))
def triangle(r):
    for i in range(1,r+1):
        print('*'*i)
triangle(a)


# In[67]:


#20. Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.
def gcd(a, b):
    gcd_value = 1
    min_num = min(a, b)
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i
    return gcd_value
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(result)


# # Advanced Level:

# In[72]:


#21. Create a program that calculates the sum of the digits of numbers in a list using a list comprehension.
numbers = [123, 456, 789]

[sum(map(int, str(num))) for num in numbers]

print("Sum of digits for each number:", sum_of_digits)


# In[73]:


#22 Write a program to find the prime factors of a given number using a `for` loop and list comprehension.
def prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

num = int(input("Enter a number to find its prime factors: "))

result = prime_factors(num)

print("Prime factors of", num, "are:", result)


# In[75]:


#23. Develop a program that extracts unique elements from a list and stores them in a new list using a list
#comprehension.
original_list = [1, 2, 3, 4, 2, 3, 5, 6, 6, 7, 8, 9, 9]
unique_elements = [x for i, x in enumerate(original_list) if original_list.index(x) == i]
print("Original list:", original_list)
print("Unique elements:", unique_elements)


# In[77]:


#24. Create a program that generates a list of all palindromic numbers up to a specified limit using a list
#comprehension.
def is_palindrome(number):
    return str(number) == str(number)[::-1]
limit = int(input("Enter the limit: "))
palindromic_numbers = [num for num in range(1, limit + 1) if is_palindrome(num)]
print("Palindromic numbers up to", limit, "are:", palindromic_numbers)


# In[86]:


#25. Write a program to flatten a nested list using list comprehension.

nested_list = [[1, 2, 3], [ 4,5, 6], 7, [8, 9]]

flattened_list = [element for sublist in nested_list for element in (sublist if isinstance(sublist, list) else [sublist])]

print("Flattened list:", flattened_list)


# In[87]:


#26. Develop a program that computes the sum of even and odd numbers in a list separately using list
#comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = sum([num for num in numbers if num % 2 == 0])
sum_odd = sum([num for num in numbers if num % 2 != 0])
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)


# In[90]:


#27. Create a program that generates a list of squares of odd numbers between 1 and 10 using list
#comprehension.
s_o=[x**2 for x in range(1,12) if x%2 !=0]
print(s_o)


# In[91]:


#28.Write a program that combines two lists into a dictionary using list comprehension.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {key: value for key, value in zip(keys, values)}
print("Combined dictionary:", combined_dict)


# In[92]:


#29. Develop a program that extracts the vowels from a string and stores them in a list using list comprehension.
input_string = "Hello World"
vowels = [char for char in input_string if char.lower() in 'aeiou']
print('vowels present in string',vowels)


# In[93]:


#30.Create a program that removes all non-numeric characters from a list of strings using list comprehension.
# List of strings containing alphanumeric characters
strings_list = ["abc123", "456def", "789ghi", "jkl"]

# Remove non-numeric characters from the list using list comprehension
numeric_strings = [''.join(char for char in string if char.isdigit()) for string in strings_list]

# Print the list with non-numeric characters removed
print("List with non-numeric characters removed:", numeric_strings)


# In[94]:


#31. Write a program to generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list
#comprehension.
def sieve_of_eratosthenes(n):
    # Create a boolean list to track prime numbers
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    # Apply the Sieve of Eratosthenes algorithm
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])
    
    # Generate the list of prime numbers using list comprehension
    prime_numbers = [i for i in range(2, n + 1) if primes[i]]
    
    return prime_numbers

# Input the upper limit for generating prime numbers
limit = int(input("Enter the upper limit for generating prime numbers: "))

# Generate the list of prime numbers using Sieve of Eratosthenes algorithm
prime_numbers = sieve_of_eratosthenes(limit)

# Print the list of prime numbers
print("List of prime numbers up to", limit, ":", prime_numbers)


# In[96]:


#32. Create a program that generates a list of all Pythagorean triplets up to a specified limit using list
#comprehension.
# Function to generate Pythagorean triplets up to a specified limit
def pythagorean_triplets(limit):
    return [(a, b, c) for c in range(1, limit + 1) for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2]

# Input the limit for generating Pythagorean triplets
limit = int(input("Enter the limit for generating Pythagorean triplets: "))

# Generate the list of Pythagorean triplets using list comprehension
triplets = pythagorean_triplets(limit)

# Print the list of Pythagorean triplets
print("List of Pythagorean triplets up to", limit, ":", triplets)


# In[98]:


#33.Develop a program that generates a list of all possible combinations of two lists using list comprehension.
# Two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

combinations = [(x, y) for x in list1 for y in list2]

print("All possible combinations of two lists:")
for combination in combinations:
    print(combination)


# In[100]:


#34. Write a program that calculates the mean, median, and mode
import numpy as np
from statistics import median, mode

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,2,2,2]

mean = np.mean(numbers)

median_value = median(numbers)
try:
    mode_value = mode(numbers)
except StatisticsError:
    mode_value = "No unique mode"
print("Mean:", mean)
print("Median:", median_value)
print("Mode:", mode_value)


# In[103]:


#35. Create a program that generates Pascal's triangle up to a specified number of rows 
def generate_pascals_triangle(rows):
    if rows == 0:
        return []

    triangle = [[1]]
    for _ in range(1, rows):
        previous_row = triangle[-1]
        new_row = [1] + [previous_row[i] + previous_row[i + 1] for i in range(len(previous_row) - 1)] + [1]
        triangle.append(new_row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))


num_rows = int(input("Enter the number of rows for Pascal's triangle: "))


triangle = generate_pascals_triangle(num_rows)


print("Pascal's triangle up to", num_rows, "rows:")
print_pascals_triangle(triangle)


# In[104]:


#36. Develop a program that calculates the sum of the digits of a factorial of numbers from 1 to 5 using list
#comprehension.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

sum_of_digits = [sum(int(digit) for digit in str(factorial(i))) for i in range(1, 6)]

for i, num in enumerate(range(1, 6), start=1):
    print("Sum of digits for factorial of", num, ":", sum_of_digits[i-1])


# In[106]:


#37. Write a program that finds the longest word in a sentence using list comprehension.
# Input sentence
sentence = input("Enter a sentence: ")
longest_word = max((word for word in sentence.split()), key=len)
print("The longest word in the sentence is:", longest_word)


# In[111]:


#38. Create a program that filters a list of strings to include only those with more than three vowels using list
#comprehension.
# Function to count vowels in a string
def count_vowels(string):
    return sum(1 for char in string if char.lower() in 'aeiou')

# List of strings
strings_list = ["aeio", "world", "python", "programming", "is", "fun"]

# Filter strings with more than three vowels using list comprehension
filtered_strings = [string for string in strings_list if count_vowels(string) > 3]

# Print the filtered list
if filtered_strings:
    print("Strings with more than three vowels:", filtered_strings)
else:
    print("No strings with more than three vowels found.")


# In[112]:


#39. Develop a program that calculates the sum of the digits of numbers from 1 to 1000 using list
#comprehension.
# Function to calculate the sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Calculate the sum of digits for numbers from 1 to 1000 using list comprehension
sum_of_digits_list = [sum_of_digits(num) for num in range(1, 1001)]

# Calculate the total sum of digits
total_sum = sum(sum_of_digits_list)

# Print the total sum of digits
print("The total sum of digits for numbers from 1 to 1000 is:", total_sum)


# In[113]:


#40. Write a program that generates a list of prime palindromic numbers using list comprehension.
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Generate list of prime palindromic numbers using list comprehension
prime_palindromes = [num for num in range(1, 1000) if is_prime(num) and is_palindrome(num)]

# Print the list of prime palindromic numbers
print("List of prime palindromic numbers:", prime_palindromes)

