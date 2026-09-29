# test 1




# def show_arguments(function):
#     def wrapper(*args, **kwargs):
#         print("Arguments:", *args)
#         return function(*args, **kwargs)

#     return wrapper


# @show_arguments
# def multiply(a, b):
#     return a * b


# first, second = (4,5)
# print(multiply(first, second))



# test 2


# def frame(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         print("==========")
#         print(result)
#         print("==========")
#     return wrapper
# @frame
# def show_text(text):
#     return text
# show_text("python")



# test 3



# def double_result(function):
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs) * 2

#     return wrapper


# @double_result
# def get_number(number):
#     return number


# print(get_number(10))



# test 4



# multiply = lambda a, b: a * b

# first, second = (6,7)
# print(multiply(first, second))



# test 5




# def count_calls(function):
#     calls = 0

#     def wrapper(*args, **kwargs):
#         nonlocal calls
#         calls += 1
#         print(f"Call: {calls}")
#         return function(*args, **kwargs)
#     return wrapper
# @count_calls
# def hello():
#     print("Hello")

# hello()
# hello()
# hello()


# test 6



# def string_only(function):
#     def wrapper(value):
#         if isinstance(value, str):
#             return function(value)
#         print("A string is required")

#     return wrapper


# @string_only
# def show(value):
#     print(value)

# show(int(input()))



# test 7



# def adult_only(function):
#     def wrapper(age):
#         if age >= 18:
#             return function(age)
#         print("Access denied")

#     return wrapper
# @adult_only
# def enter_club(age):
#     print("Welcome")

# enter_club(int(input()))
# enter_club(int(input()))



# test 8


# students = [('Ali', 75), ('Sara', 92), ('Bob', 84)]
# sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
# print(sorted_students)



# test 9


# def add_prefix(function):
#     def wrapper(*args, **kwargs):
#         return "Result: " + function(*args, **kwargs)

#     return wrapper
# @add_prefix
# def get_name(name):
#     return name
# print(get_name("Ali"))




#  test 10




# def check_division(function):
#     def wrapper(a, b):
#         if b == 0:
#             print("Cannot divide by zero")
#             return None
#         return function(a, b)

#     return wrapper


# @check_division
# def divide(a, b):
#     return a / b

# dividend, divisor = (10,0)
# result = divide(dividend, divisor)
# if result is not None:
#     print(result)



# test 11


# numbers = (-4,7,0,-2,9,3)
# positive_numbers = list(filter(lambda number: number > 0, numbers))
# print(positive_numbers)

