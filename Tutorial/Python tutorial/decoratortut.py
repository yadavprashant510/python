print("Started")
from functools import wraps
print("---------------------------------------------1.Program------------------------------------")
def smart_div(func):
    """Divide smartly"""
    @wraps(func)
    def wrapper(a,b):
        if b == 0:
            print(f"Division is not possible because b is equal to {b}")
        else:
            func(a,b)

    return wrapper


def division(a,b):
    print(f"Division of  {a} / {b} is :  {a / b} ")

div = smart_div(division)
div(20,5)
div(20,0)
div(100,5)


# print("---------------------------------------------2.Program------------------------------------")
#
# def hello_function():
#     def say_hi():
#         print("Hi")
#     return say_hi
#
#
# hello = hello_function()
# hello()
#
# print("---------------------------------------------3.Program------------------------------------")


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         print(make_uppercase)
#         return make_uppercase
#
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     # print('hello there')
#     return "hello there"
#
#
# decorate = uppercase_decorator(say_hi)
# say_hi()

# print("------------------------------------4.Program-----------------------------------------")


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         print(make_uppercase)
#         return make_uppercase
#
#     return wrapper


# def split_string(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         print(splitted_string)
#         return splitted_string
#     return wrapper
#
#
# @split_string
# @uppercase_decorator
# def say_hi():
#     return 'hello world'
#
#
# say_hi()
# print("Completed")


# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(args1,args2):
#         print(f"My arguments are: {args1}, {args2}")
#         function(args1, args2)
#
#     return wrapper_accepting_arguments
#
#
# @decorator_with_arguments
# def cities(city_one, city_two):
#     print(f"Cities I love are {city_one} and {city_two}")
#
#
# cities("Nairobi", "England")


# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#         print('The positional arguments are',args)
#         print('The keyword arguments are',kwargs)
#         function_to_decorate(*args)

#     return a_wrapper_accepting_arbitrary_arguments


# # @a_decorator_passing_arbitrary_arguments
# # def function_with_no_argument():
# #     print("No arguments here.")
# #
# # function_with_no_argument()

# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a,b,c):
#     print(a,b,c)


# function_with_arguments(1,2,3)


# @a_decorator_passing_arbitrary_arguments
# def function_with_keyword_arguments():
#     print("This has shown keyword arguments")


# function_with_keyword_arguments(first_name="Derrick",last_name="Mwiti")

import time
from functools import wraps
def timethis(func):
    '''Decorator that reports the excecution times'''
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    """Counts down"""
    while n>0:
        n-=1
countdown(500)

