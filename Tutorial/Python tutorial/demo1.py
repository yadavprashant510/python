# string = 'B4A15PK9K6D3'
# # output ="ABD134"
# s1 = s2 = output =''
# for w in string:
#     if w.isalpha():
#         s1 = s1+w
#     else:
#         s2 = s2+w
# for w in sorted(s1):
#     output = output+w
# for w in sorted(s2):
#     output = output+w
# assert output ,'ABDKKP134569'
# print(output)

# input = a4b3c2
# output = aaaabbbcc
# output = ''
# string = 'a2k4b3c2'

# for s in string:
#     if s.isalpha():
#         output = output+s
#         previous = s
#     else:
#         output = output + previous*(int(s)-1)
# print(output, output)

# color_bars = Fore.GREEN
# for i in trange(100, desc="Loading...", bar_format ="{l_bar}%s{bar}%s{r_bar}" %(color_bars)):
#     time.sleep(0.3)
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
text = ""


# for char in tqdm(["a", "b", "c", "d"]):
#     time.sleep(0.25)
#     text = text + char
# print(text)

# pbar = tqdm(["a", "b", "c", "d"])
# for char in pbar:
#     time.sleep(0.25)
#     pbar.set_description("Processing %s" % char)
#
# with tqdm(total = 100) as pbar:
#     for i in range(10):
#         print(str(i))
#         time.sleep(0.1)
#         pbar.update(10)


# def csv_writer(f_name: str, l_name: str):
#     with open('Test.csv', mode = 'w', newline = '') as file:
#         header = ["First_Name", "Last_Name"]
#         writer = csv.writer(file, dialect = "excel")
#         writer.writerow(header)
#         writer.writerow([f_name, l_name])
#
#
# csv_writer('Ankur', 'Yadav')
# csv_writer('Prashant', 'Yadav')
#
# print("Date:", '12-02-2020', end = "  ")
# print("In_time:", '12:56', end = " ")
# print("Out_time:", '09:00')
# print("Date:", '12-02-2020', end = "  ")
# print("In_time:", '12:56', end = " ")
# print("Out_time:", '09:00', end = " ")
