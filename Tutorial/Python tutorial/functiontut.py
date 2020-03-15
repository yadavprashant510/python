import glob
import os
import time

python_file = glob.glob("*.py")
name_sz_date = [(name, os.path.getsize(name),
                 os.path.getmtime(name)) for name in python_file]
for name, size, mod_time in name_sz_date:
    print(f"File Name :{name}\nFile Size :{size / 1024} KB\
        \nModification Time : {time.ctime(mod_time)}")
