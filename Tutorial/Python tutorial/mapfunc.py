
# def addition(n):
#     """ Take number as input and return double of that number"""
#     return n+n
# # map functon is used to apply function to each element in list


# num = [1,2,3,4]
# # double = list(map(addition,num))
# # print(double)
# # We can also write this code using lambda function
# double = list(map(lambda x:x*x,num))
# print(double)
#
# # Add two list usin map and lambda
# num1 = [1,2,3]
# num2 = [4,5,6]
# added_list = list(map(lambda x,y:x+y,num1,num2))
# print(added_list)
# ---------------------------temp_converter---------------------
# def fahrenheit(T):
#     return ((float(9)/5)*T+32)
#
# def celsius(T):
#     return (float(5)/9)*(T-32)
#
# temp = [36.5,37,37.5,38,39]
# # F = map(fahrenheit,temp)
# # C = map(celsius,temp)
# temp_in_Fahrenheit = list(map(fahrenheit,temp))
# temp_in_Celsius = list(map(celsius,temp_in_Fahrenheit))
# print(temp_in_Celsius)
# print(temp_in_Fahrenheit)
# ----------------------------map and lambda function together------------------
# a = [1, 2, 3, 4]
# b = [17, 12, 11, 10]
# c = [-1, -4, 5, 9]
#
# sum = list(map(lambda x,y:x+y,a,b))
# print(sum)
# sum_of_three =list(map(lambda x,y,z:x+y+z,a,b,c))
# print(sum_of_three)



