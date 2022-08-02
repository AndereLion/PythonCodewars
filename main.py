# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
#
# Examples:
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5

# def is_divisible(n, x, y):
#     if n % x == 0 and n % y == 0:
#         return f'true because {n} is divisible by {x} and {y}'
#     elif n % x == 0:
#         return f'false because {n} is not divisible by {y}'
#     elif n % y == 0:
#         return f'false because {n} is not divisible by {x}'
#     else:
#         return f'false because {n} is neither divisible by {x} nor {y}'
# def find_missing_letter(chars):
#     n = 0
#
#     while ord(chars[n]) == ord(chars[n + 1]) - 1:
#         n += 1
#
#     return chr(1 + ord(chars[n]))
#
#
# print(find_missing_letter(["o", "q", "e", "s"]))

# def unique_in_order(iterable):
#     if len(iterable) > 0:
#         result = [iterable[0]]
#     else:
#         result = []
#     for ind in range(len(iterable) - 1):
#         if ord(str(iterable[ind])) == ord(str(iterable[ind + 1])):
#             continue
#         result.append(iterable[ind + 1])
#     return result
#
#
# print(unique_in_order('ABBCcAD'))
#
# print(unique_in_order([1, 2, 2, 3, 3, 4]))

# def race_podium(blocks):
#     if blocks != 7:
#         result = [(blocks / 3).__ceil__()]
#     else:
#         result = [2]
#     blocks -= result[0]
#     first = result[0]
#     while first <= result[0] or result[0] <= blocks - first:
#         first += 1
#     result.append(first)
#     result.append(blocks - first)
#
#     return tuple(result)
#
#
# print(race_podium(11))
# print(race_podium(6))
# print(race_podium(10))
# print(race_podium(6))
# print(race_podium(7))
# print(race_podium(49))
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.
# test.assert_equals(make_readable(0), "00:00:00")
# test.assert_equals(make_readable(5), "00:00:05")
# test.assert_equals(make_readable(60), "00:01:00")
# test.assert_equals(make_readable(86399), "23:59:59")
# test.assert_equals(make_readable(359999), "99:59:59")

# def make_readable(seconds):
#     h = 0
#     m = 0
#
#     if seconds >= 3600:
#         h = seconds // 3600
#         seconds = seconds - (h * 3600)
#
#     if seconds >= 60:
#         m = seconds // 60
#         seconds = seconds - (m * 60)
#
#     if len(str(h)) == 1:
#         h = '0' + str(h)
#     else:
#         h = str(h)
#     if len(str(m)) == 1:
#         m = '0' + str(m)
#     else:
#         m = str(m)
#     if len(str(seconds)) == 1:
#         seconds = '0' + str(seconds)
#     else:
#         seconds = str(seconds)
#     return f"{h}:{m}:{seconds}"
#
#
# print(make_readable(43272))
#######################################################################
# Task
# Sum all the numbers of a given array ( cq. list ),
# except the highest and the lowest element ( by value, not by index! ).
#
# The highest or lowest element respectively is a single element at each edge,
# even if there are more than one with the same value.
#
# Mind the input validation.
#
# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation
# If an empty value ( null, None, Nothing etc. ) is given instead of an array,
# or the given array is an empty list or a list with only 1 element, return 0.
# import codewars_test as test
# from solution import sum_array
#
#
# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('None or Empty')
#     def basic_test_cases():
#         test.assert_equals(sum_array(None), 0)
#         test.assert_equals(sum_array([]), 0)
#
#     @test.it("Only one Element")
#     def one_test_cases():
#         test.assert_equals(sum_array([3]), 0)
#         test.assert_equals(sum_array([-3]), 0)
#
#     @test.it("Only two Element")
#     def two_test_cases():
#         test.assert_equals(sum_array([3, 5]), 0)
#         test.assert_equals(sum_array([-3, -5]), 0)
#
#     @test.it("Real Tests")
#     def real_test_cases():
#         test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
#         test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
#         test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
#         test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)
# def sum_array(arr):
#     if type(arr) != list:
#         return 0
#     if len(arr) <= 1:
#         return 0
#     arr.remove(max(arr))
#     arr.remove(min(arr))
#     return sum(arr)
#
#
# print(sum_array([6, 2, 1, 8, 10]))
############################################################
# Write a generic function chainer
# Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).
#
# The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.
#
# def add10(x): return x + 10
# def mul30(x): return x * 30
#
# chain(50, [add10, mul30])
# # returns 1800
# def add10(x): return x + 10
# def mul30(x): return x * 30
#
#
# @test.describe("Test")
# def test_group():
#     @test.it("Sample tests")
#     def test_case():
#         test.assert_equals(chain(42, []), 42)
#         test.assert_equals(chain(50, [mul30]), 1500)
#         test.assert_equals(chain(50, [mul30, add10]), 1510)
#         test.assert_equals(chain(50, [add10, mul30]), 1800)

# def add10(x): return x + 10
#
#
# def mul30(x): return x * 30
#
#
# def chain(init_val, functions):
#     if len(functions) > 0:
#         for func in functions:
#             init_val = func(init_val)
#     return init_val
#
#
# print(chain(42, []))
# print(chain(50, [mul30]))
############################################
# The maximum sum subarray problem consists in
# finding the maximum sum of a contiguous subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.
# test.describe("Tests")
# test.it('should work on an empty array')
# test.assert_equals(max_sequence([]), 0)
# test.it('should work on the example')
# test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
# import string
#
#
# def position(alphabet):
#     return string.ascii_letters.index(alphabet)+1
# print(position('a'))
###########################################
# Funny Dots
# You will get two integers n (width) and m (height) and your task is to draw the following pattern. Each line is seperated with a newline (\n)
#
# Both integers are equal or greater than 1; no need to check for invalid parameters.
#
# Examples
#
#                                             +---+---+---+
#              +---+                          | o | o | o |
# dot(1, 1) => | o |            dot(3, 2) =>  +---+---+---+
#              +---+                          | o | o | o |
#                                             +---+---+---+
# def dot(n, m):
#     result = ''
#     for v in range(m):
#         result += n * '+---' + '+' + '\n'
#         result += n * '| o ' + '|' + '\n'
#
#     result += n * '+---' + '+' + '\n'
#
#     return result
#
#
# print(dot(1, 1))
#
# '+---+---+---+\n| o | o | o |\n+---+---+---+\n| o | o | o |\n+---+---+---+\n' should equal
# '+---+---+---+\n| o | o | o |\n+---+---+---+\n| o | o | o |\n+---+---+---+'
#################################################
# def find_function(func, arr):
#     for v in func:
#         if type(v) != int or type(v) != str:
#             return list(filter(v, arr))
#
#
# print(find_function([9, 3, lambda a: a % 2, 1, 0], [1, 2, 3, 4]))
##########################################################
# Convert text to brainfuck
# You are tasked to writting a function to_brainfuck/toBrainfuck that converts a given string to brainfuck
# that would print the given string.
# For example if we were to call to_brainfuck("Hello World!") it might give us a result
# that is something like:
# "-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[--->+<]>-----.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>."
# , if we execute that code we would get "Hello World!" at the output.
# import codewars_test as test
# from solution import to_brainfuck
# from preloaded import brainfuck_interpreter
#
#
# @test.describe("Sample Tests")
# def sample_tests():
#     @test.it("Fixed Tests")
#     def test_case():
#         test.assert_equals(brainfuck_interpreter(to_brainfuck("Hello World!")), "Hello World!")
#         test.assert_equals(brainfuck_interpreter(to_brainfuck("Bye bye birdy")), "Bye bye birdy")

# def is_opposite(s1, s2):
#     # print(s1.isupper())
#     # print(s1.islower())
#     # print(s1.isalpha())
#     # print(s1.isalnum())
#     # print(s1.isascii())
#     # print(s1.isidentifier())
#     # print(s1.isprintable())
#     # print(s1[0] == s2[0])
#     print(s1.swapcase())
#     if len(s1) < 1:
#         return False
#
#     for ind in range(len(s1)):
#
#         if s1[ind].islower() == s2[ind].islower():
#             return False
#
#     return True
#
#
# print(is_opposite("ab", "AB"))
# print(is_opposite("aB", "Ab"))
# print(is_opposite("aBcd", "AbCD"))
# print(is_opposite("AB", "Ab"))
# print(is_opposite("", ""))


# test.assert_equals(is_opposite("ab", "AB"), True);
# test.assert_equals(is_opposite("aB", "Ab"), True);
# test.assert_equals(is_opposite("aBcd", "AbCD"), True);
# test.assert_equals(is_opposite("AB", "Ab"), False);
# test.assert_equals(is_opposite("", ""), False);
#############################################
# def index(array, n):
#     return (array[n] ** n) if len(array) > n else -1
#
#
# print(index([1, 2, 3, 4], 4))
#
# print(index([1, 3, 10, 100], 3))
##################################################
# import decimal
# import math
# #
# from decimal import *
# import math
#
# getcontext().prec = 1000
# from decimal import *
#
# getcontext().prec = 1000
#
#
# def fibonacci(n):
#     return int(Decimal((Decimal(1) / Decimal(5).sqrt()) * (
#                 (((Decimal(1) + Decimal(5).sqrt()) / Decimal(2)) ** Decimal(n)) - (
#                     ((Decimal(1) - Decimal(5).sqrt()) / Decimal(2)) ** Decimal(n)))))


# def fibonacci(n):
# a = 0
# b = 1
# if n == 1:
#     return 1
# for i in range(n-1):
#     b = a + b
#     a = b - a
#
# return b

# return int(Decimal((Decimal(1) / Decimal(Decimal(5).sqrt())) * (
#             (((Decimal(1) + Decimal(Decimal(5).sqrt())) / Decimal(2)) ** Decimal(n)) - (
#                 ((Decimal(1) - Decimal(Decimal(5).sqrt())) / Decimal(2)) ** Decimal(n)))))


#
#
# print(fibonacci(925))
# print(fibonacci(70))
# # 190392490709135
# # 308061521170129
# print(fibonacci(60))
# print(fibonacci(50))
######################################################
# My friend John and I are members of the "Fat to Fit Club (FFC)".
# John is worried because each month a list with the weights of members is published and
# each month he is the last on the list which means he is the heaviest.
#
# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list".
# It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.
#
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
#
# Given a string with the weights of FFC members in normal order
# can you give this string ordered by "weights" of these numbers?
#
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:
#
# "100 180 90 56 65 74 68 86 99"
# When two numbers have the same "weight",
# let us class them as if they were strings (alphabetical ordering) and not numbers:
#
# 180 is before 90 since, having the same "weight" (9), it comes before as a string.
#
# All numbers in the list are positive numbers and the list can be empty.
#
# Notes
# it may happen that the input string have leading,
# trailing whitespaces and more than a unique whitespace between two consecutive numbers
# For C: The result is freed.

# def order_weight(strng):
#     list_of_weights = strng.split()
#     for i1 in range(len(list_of_weights)):
#         for i2 in range(len(list_of_weights) - 1):
#             if sum([int(v) for v in list_of_weights[i2]]) > sum([int(v) for v in list_of_weights[i2 + 1]]):
#                 tmp = list_of_weights[i2]
#                 list_of_weights[i2] = list_of_weights[i2 + 1]
#                 list_of_weights[i2 + 1] = tmp
#
#     for i1 in range(len(list_of_weights)):
#         for i2 in range(len(list_of_weights) - 1):
#             if sum([int(v) for v in list_of_weights[i2]]) == sum([int(v) for v in list_of_weights[i2 + 1]]):
#                 if int(list_of_weights[i2][0]) > int(list_of_weights[i2 + 1][0]):
#                     tmp = list_of_weights[i2]
#                     list_of_weights[i2] = list_of_weights[i2 + 1]
#                     list_of_weights[i2 + 1] = tmp
#########################################################
# Calculate how many times a number can be divided by a given number.
#
# Example
# For example the number 6 can be divided by 2 two times:
#
# 1. 6 / 2 = 3
# 2. 3 / 2 = 1 remainder = 1
# 100 can be divided by 2 six times:
#
# 1. 100 / 2 = 50
# 2. 50 / 2 = 25
# 3. 25 / 2 = 12 remainder 1
# 4. 12 / 2 = 6
# 5. 6 / 2 = 3
# 6. 3 / 2 = 1 remainder 1

# def divisions(n, divisor):
#     result = 0
#     while divisor <= n:
#         print(n)
#         n /= divisor
#         result += 1
#     return result
#
#
# print(divisions(2450, 5))
#
# # test.assert_equals(divisions(6, 2), 2)
# # test.assert_equals(divisions(100, 2), 6)
# # test.assert_equals(divisions(2450, 5), 4)
# # test.assert_equals(divisions(9999, 3), 8)
# # test.assert_equals(divisions(2, 3), 0)
# # test.assert_equals(divisions(5, 5), 1)
# #
# #     return ' '.join(list_of_weights)
# #
# #
# # print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))
# # #
# # # test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
# # # test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"),
# # #                    "11 11 2000 10003 22 123 1234000 44444444 9999")
# # # test.assert_equals(order_weight(""), "")
################################################################
# Given a positive integer return the closest integer to it that is divisible by 10.
#
# Example input:
#
# 22
# 25
# 37
# Expected output:
#
# 20
# 30
# 40
# def closest_multiple_10(i):
#     if i < 10:
#         return 10
#     while i % 10 != 0:
#         if i % 10 >= 5:
#             i += 1
#         else:
#             i -= 1
#     return i
import math

#
# def closest_multiple_10(i):
#     if i < 10:
#         i = 10
#
#     return i + (10 - i % 10) if i % 10 > 4 else i - i % 10
#
# def closest_multiple_10(i):
#     return round(i,-1)
#
# print(closest_multiple_10(11))
# print(closest_multiple_10(59))
#######################################
# See example:
#
# Input:
# [5, 10, 6]  >>> This represents:
#            # citizen 1 has wealth 5
#            # citizen 2 has wealth 10
#            # citizen 3 has wealth 6
# Should be after the test:
#  [7, 7, 7] >>> wealth has now been equally redistributed
# Info:
#
# MUTATE the input array/list, don't return anything
# Input is guaranteed to hold at least 1 citizen
# Wealth of a citizen will be an integer with minimum equal to 0 (negative wealth is not possible)
# Handling of floating point error will not be tested
# wealth_equal = [5, 5, 5, 5, 4]
#

# def redistribute_wealth(wealth):
#
#     wealth = [sum(wealth) / len(wealth) for i in range(len(wealth))]
#
#
#
# answer = redistribute_wealth(wealth_equal)
# print(wealth_equal)
# if answer is None:
#     print("Don't return anything!")
# def redistribute_wealth(wealth):
#     wealth_copy = wealth.copy()
#     return [sum(wealth_copy) / len(wealth_copy) for i in range(len(wealth_copy))]
# def redistribute_wealth(wealth):
#     average = sum(wealth) / len(wealth)
#     result = []
#     for i in range(len(wealth)):
#         result.append(average)
#     return result
#
#
# print(redistribute_wealth([5, 5, 5, 5, 5]))
# print(redistribute_wealth([0, 10]))
# print(redistribute_wealth([5]))
# print(redistribute_wealth([3, 2, 2]))
####################################
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
#
# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0
# Waiting for translations and Feedback! Thanks!
# def paperwork(n, m):
#     return n * m if not (n < 0 or m < 0) else 0
#
#
# print(paperwork(5, 5))
##################################
# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
# def count_positives_sum_negatives(arr):
#     if len(arr) == 0:
#         return arr
#     if max(arr) == 0:
#         return [0, 0]
#
#     return [len(list(filter(lambda x: (x > 0), arr))), sum(list(filter(lambda x: (x < 0), arr)))]
#
#
# print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
###############################################
# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
#
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
# Note for Go
# For Go: Empty string slice is expected when there are no anagrams found.
#
# def anagrams(word: str, words: []):
#     words_result = words.copy()
#
#     for i, string in enumerate(words):
#
#         if len(string) != len(word):
#             words_result.remove(string)
#         for ind, char in enumerate([char for char in string]):
#             if word.count(char) != string.count(char):
#                 try:
#                     words_result.remove(string)
#                 except:
#                     pass
#     return words_result

# def anagrams(word: str, words: []):
#
#     return list(filter(lambda x: sorted(word) == sorted(x), words))
#
#
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
###################################
# def even_or_odd(number):
#     return 'Even' if number % 2 == 0 else 'Odd'
#
#
# print(even_or_odd(2))
# print(even_or_odd(3))
# print(even_or_odd(1))
# print(even_or_odd(0))
################################

# def test(A, B):
#     for i in enumerate(B):
#         if max(B) >= A:
#             B.remove(max(B))
#         else:
#             return max(B)
#
#
# print(test(13, [3, 5, 7, 4, 11, 13]))
###########################################
# Let's imagine we have a popular online RPG. A player begins with a score of 0 in class E5.
# A1 is the highest level a player can achieve.
#
# Now let's say the players wants to rank up to class E4.
# To do so the player needs to achieve at least 100 points to enter the qualifying stage.
#
# Write a script that will check to see if the player has achieved at least 100 points in his class.
# If so, he enters the qualifying stage.
#
# In that case, we return, "Well done! You have advanced to the qualifying stage.
# Win 2 out of your next 3 games to rank up.".
#
# Otherwise return, False/false (according to the language in use).
#
# NOTE
# : Remember, in C# you have to cast your output value to Object type!
# def playerRankUp(pts: int):
#     text = "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
#     return text if pts >= 100 else False
#
#
# print(playerRankUp(100))
# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# def solution(A):
#     test = list(set(A))
#     result = 1
#     for i in range(len(test) - 1):
#         if test[i] > 0:
#             if test[i + 1] - test[i] != 1:
#                 result = test[i] + 1
#                 break
#     if result == 1:
#         if test[0] == 1:
#             result = max(test) + 1
#     return result
#
#
# print(solution([1, 3, 6, 4, 1, 2, 11, 7]))
#######################################
# def solution(A):
#     result = []
#     for i, v in enumerate(A):
#         if result.count(v) == 0:
#             result.append(v)
#
#     return result
#
#
# print(solution([1, 4, 7, 9,4, 5, 3]))
# import math
# def solution(S):
#     result = S.split(',')
#     result2 = []
#     for i, v in enumerate(result):
#         try:
#             result2.append(float(v))
#         except:
#             pass
#     return 0 if len(result2) == 0 else math.floor(sum(result2) / len(result2))
#
# print(solution('1.5, 3, 5, 6.5'))
# print(solution('1.5, 3, 5, 6.5,444444'))
# print(solution('g,hj,k,l'))
######################################
# There exist two zeroes: +0 (or just 0) and -0.
#
# Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).
#
# In JavaScript / TypeScript / Coffeescript the input will be a number.
#
# In Python / Java / C / NASM / Haskell / the input will be a float.
# def is_negative_zero(n):
#     return True if n == 0 and str(n)[0] == '-' else False
#
#
# print(is_negative_zero(-0.0))
# print(is_negative_zero(0.0))
# print(is_negative_zero(-3.0))
#########################
# def reverse_list(lst):
#     return lst[::-1]
#
#
# print(reverse_list([3, 5, 7, 8, 4, 6]))
######################################
# Write a function partlist that gives all the ways to divide a list (an array)
# of at least two elements into two non-empty parts.
#
# Each two non empty parts will be in a pair
# (or an array for languages without tuples or a structin C - C: see Examples test Cases - )
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
# Examples of returns in different languages:
# a = ["az", "toto", "picaro", "zone", "kiwi"] -->
# [["az", "toto picaro zone kiwi"], ["az toto", "picaro zone kiwi"],
# ["az toto picaro", "zone kiwi"], ["az toto picaro zone", "kiwi"]]
# def partlist(arr):
#     first_part = ''
#     second_part = ''
#     for i, v in enumerate(arr):
#         if i <= len(arr) / 2:
#             first_part += v
#         else:
#             second_part += v
#     return [first_part, second_part]
#
#
# print(partlist(["I", "wish", "I", "hadn't", "come"]))
############################
# Help Suzuki rake his garden!
#
# The monastery has a magnificent Zen garden made of white gravel and rocks and
# it is raked diligently everyday by the monks. Suzuki having a keen eye is
# always on the lookout for anything creeping into the garden that must be removed
# during the daily raking such as insects or moss.
#
# You will be given a string representing the garden such as:
#
# garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant
# gravel gravel snail rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant
# gravel gravel gravel gravel rock slug gravel gravel gravel gravel gravel snail gravel gravel
# rock gravel snail slug gravel gravel spider gravel gravel gravel gravel gravel gravel gravel
# gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel gravel moss gravel gravel
# gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel
# gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider gravel rock gravel gravel'
# Rake out any items that are not a rock or gravel and replace them with gravel such that:
#
# garden = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
# Returns a string with all items except a rock or gravel replaced with gravel:
#
# garden = 'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'
# def rake_garden(garden):
#     result = [i for i in garden.split()]
#     for i, v in enumerate(result):
#         if v != 'rock' and v != 'gravel':
#             result[i] = 'gravel'
#     return ' '.join(result)
#
#
# print(rake_garden('rock gravel jgdgd gravel rock gravel gravel gravel gravel gravel gravel gravel'))
##########################
# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# def xo(s):
#     if s.lower().count('x') == 0 and s.lower().count('o') == 0:
#         return True
#     return True if s.lower().count('x') == s.lower().count('o') else False
#
#
# print(xo("ooxx"))
# print(xo("xooxx"))
# print(xo("ooxXm"))
# print(xo("zpzpzpp"))
# print(xo(("zzoo")))
############################
# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]
# def maps(a):
#     return [i * 2 for i in a]
#
# print(maps([1, 2, 3]))
###########################
# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
# def square_sum(numbers):
#     return sum([i ** 2 for i in numbers])
#
# print(square_sum([1, 2, 2]))
#######################################
# def no_space(x):
#     return x.replace(' ', '')
#
# print(no_space('dfgdgdg dgdgdd'))
#######################################
# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.
# def positive_sum(arr):
#     return sum([i for i in arr if i > 0])
#
# print(positive_sum([1, -4, 7, 12]))
####################################
# Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots.
# i.e.
#
# 1st (1)   2nd (3)    3rd (6)
# *          **        ***
#            *         **
#                      *
# You need to return the nth triangular number. You should return 0 for out of range values:
#
# For example: (Input --> Output)
#
# 0 --> 0
# 2 --> 3
# 3 --> 6
# -10 --> 0
# Bad performance !!!!
# def triangular(n):
#     if n <= 0:
#         return 0
#     result = 1
#     for i in range(1, n):
#         result += i + 1
#     return result
# from decimal import *
#
# getcontext().prec = 100
#
#
# def triangular(n):
#     return int(Decimal(Decimal(n) * Decimal(n) / Decimal(2) + (Decimal(n) / Decimal(2)))) if n > 0 else 0
#
#
# print(triangular(555555555555555))
# print(triangular(2))
# print(triangular(3))
# print(triangular(4))
# print(triangular(5))
# print(triangular(6))

# 3/6
# ***
# **
# *
# 4/10
# ****
# ***
# **
# *
# 5/15
# *****
# ****
# ***
# **
# 6/21
# ******
# *****
# ****
# ***
# **
# *
######################################
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return True if you're better, else False!
#
# Note:
# Your points are not included in the array of your class's points.' \
# ' For calculating the average point you may add your point to the given array!
#
# def better_than_average(class_points, your_points):
#     return True if sum(class_points) / len(class_points) < your_points else False
#
# print(better_than_average([2, 3, 6], 5))
######################################
# f herdeon(a, b, c):
#     s = (a + b + c) / 2
#     return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 2)
#
#
# print(heron(3, 4, 5))
###########################################
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or
# exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.
#
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false
# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         try:
#             [int(v) for v in pin]
#             return True
#         except:
#             return False
#     else:
#         return False
# Second
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
#
#
# print(validate_pin('4444'))
# print(validate_pin('55555'))
# print(validate_pin('1234b'))
# print(validate_pin('a1234'))
# print(validate_pin('666666'))
#######################
# The new £5 notes have been recently released in the UK and they've certainly became a sensation!
# Even those of us who haven't been carrying any cash around for a while,
# having given in to the convenience of cards, suddenly like to have some of these in
# their purses and pockets. But how many of them could you get with what's left from your
# salary after paying all bills? The programme that you're about to write will count this for you!
#
# Given a salary and the array of bills, calculate your disposable income for a month and return it as a number of new £5 notes you can get with that amount. If the money you've got (or do not!) doesn't allow you to get any £5 notes return 0.
#
# £££ GOOD LUCK! £££
# import math
#
#
# def get_new_notes(salary, bills):
#     return math.floor((salary - sum(bills)) / 5) if math.floor((salary - sum(bills)) / 5) > 0 else 0
#
#
# print(get_new_notes(2000, [500, 160, 400]))
########################
# def calculate_distance(r):
#     return r * -1.63299
#
#
# print(calculate_distance(10))
#
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
#
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
# and month 11 (November), is part of the fourth quarter.
# def quarter_of(month):
#     if 0 < month / 3 <= 1:
#         return 1
#     elif 1 < month / 3 <= 2:
#         return 2
#     elif 2 < month / 3 <= 3:
#         return 3
#     elif 3 < month / 3 <= 4:
#         return 4
#
# print(quarter_of(12))
########################
# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]
# def maps(a):
#     return [v * 2 for v in a]
#
#
# print(maps([1, 2, 3]))
#########################
# In this simple exercise, you will build a program that takes a value, integer ,
# and returns a list of its multiples up to another value, limit . If limit is
# a multiple of integer, it should be included as well. There will only ever be positive integers
# passed into the function, not consisting of 0. The limit will always be higher than the base.
#
# For example, if the parameters passed are (2, 6), the function should
# return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
#
# If you can, try writing it in only one line of code.
# def find_multiples(integer, limit):
#     return [v for v in range(integer, limit, integer)]
#
#
# print(find_multiples(2, 12))
# print(find_multiples(5, 25))

##################################
"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)
4 --> 3 (1, 2, 4)
5 --> 2 (1, 5)
12 --> 6 (1, 2, 3, 4, 6, 12)
30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
"""


#
#
# def divisors(n):
#     return len([v for v in range(1, n+1) if n % v == 0])
#
#
# print(divisors(5))
# def sum_corners(n):
#     return int(1 + (n * n / 2 + (n / 2) - n + 1) + (n * n / 2 + (n / 2)))
#
#
# print(sum_corners(3))
###########################
# def sum_mix(arr):
#     return sum([int(v) for v in arr])
#
#
# print(sum_mix([1, 2, 3, 4, '5', '6']))
#############################
# Given a mixed array of number and string representations of integers,
# add up the string integers and subtract this from the total of the non-string integers.
#
# Return as a number.
# def div_con(x):
#     int_numbers = []
#     str_numbers = []
#     for v in x:
#         if type(v) == int:
#             int_numbers.append(v)
#         else:
#             str_numbers.append(int(v))
#     return sum(int_numbers) - sum(str_numbers)
#####
# def div_con(x):
#     int_numbers = [v for v in x if type(v) == int]
#     str_numbers = [int(v) for v in x if type(v) == str]
#     return sum(int_numbers) - sum(str_numbers)
#
#
# print(div_con([9, 3, '7', '3']))
########################################

# def words_to_marks(s):
#     result = 0
#     for i, v in enumerate(s.lower()):
#         result += ord(v) - 96
#     return result
#
#
# print(words_to_marks('love'))
###################################
# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
# def solution(string, ending):
#     if ending == '':
#         return True
#     if len(ending) > len(string):
#         return False
#     string = string[::-1]
#     ending = ending[::-1]
#     for i, v in enumerate(ending):
#         if v != string[i]:
#             return False
#
#     return True
#
#
# print(solution('sumo', 'mommfmf'))
