import os

data = ['ACME', 50, 91.1, (2012,2,21)]
name, shares, price, date = data
# print(name, shares, price, date)

files = os.listdir()
files = [file for file in files if file.endswith(".py")]
print(f"Files --> {files}")
print(f"No of file --> {len(files)}")
# files = os.listdir()
# for file in files:
#     if str(file).endswith(".txt"):
#         print(f"File is --> {file}")
