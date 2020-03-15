import os

file_name = [file for file in os.listdir("F:\PRICE REFRESH\Blocked")]
print(file_name)
ls = [i for i in range(100) if i % 3 == 0]
print(ls)
# dictionary comprehension
dict1 = {i: f"item {i}" for i in range(1, 100)
         if i % 3 == 0}
print(dict1)
dict1 = {i: f"item {i}" for i in range(1, 10)
         }
dict2 = {value: key for key, value in dict1.items()}
print(dict1, "\n", dict2)

# generator comprehension

evens = (i for i in range(10) if
         i % 2 == 0)
for item in evens:
    print(item)
