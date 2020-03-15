
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"D:\Python\Python37\Tesseract OCR\tesseract.exe"
# print(pytesseract.image_to_string(Image.open('pancard_vishal.jpg')))
# print(pytesseract.image_to_boxes

# print(pytesseract.image_to_string())
import os
import os.path
import json
import sys
import pytesseract
import re
import difflib
import csv
import dateutil.parser as dparser
try:
    from PIL import Image
except ImportError:
    print("Please install PIL package")
    sys.exit()

# extracting text from image using tesseract
text = pytesseract.image_to_string(Image.open('pancard_vishal.jpg'))

# Initializing data variable
name = None
fname = None
dob = None
pan = None
nameline = []
dobline = []
panline = []
text0 = []
text1 = []
text2 = []
govRE_str = '(GOVERNMENT|GOVT.|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT\
             |PARTMENT|ARTMENT|INDIA|NDIA)$'
numRE_str = '(Number|umber|Account|ccount|count|Permanent|\
             ermanent|manent)$'

# Searching for PAN
lines = text.split('\n')
for lin in lines:
    s = lin.strip()
    s = s.rstrip()
    s = s.lstrip()
    text1.append(s)

# print("Text1:",text1)
# lineno = 0

for wordline in text1:
    xx = wordline.split()
    if [w for w in xx if re.search(govRE_str, w)]:
        lineno = text1.index(wordline)
        break

raw_text = text1[lineno+2:]
clean_data = []
for rdata in raw_text:
    if rdata =="":
        continue
    else:
        clean_data.append(rdata)
for raw_dat in clean_data:
    m = re.findall(r'\d\d/\d\d/\d{4}',raw_dat)
    if m !=[]:
      dob = m


clean_string = [x.strip() for x in str(raw_text).split(",")]
# print("String after removing redundant data:",raw_text)
# print("Clean data:",clean_data)

try:
    full_name = clean_data[0]
    lname = full_name.split()[0]
    assert full_name == 'YADAV PRASHANT SHYAMNARAYAN'

    name = full_name.split()[1]
    print(f"Name:{name} {lname}")
    fname = full_name.split()[2]
    assert fname == 'SHYAMNARAYAN'
    print(f"Father Name:{fname} {lname}")

    print(f"Last name:{lname}")
    print(f"DOB:{dob[0]}")

except Exception as e:
    print("Exception occured.")

try:
    dobline = [item for item in text0 if item not in nameline]
    # print("Dobline:", m)
    for x in dobline:
        z = x.split()
        z = [s1 for s1 in z if len(s1) > 3]
        for y in z:
            if dparser.parse(y, fuzzy=True):
                dob = dparser.parse(y, fuzzy=True).year
                panline = dobline[dobline.index(x) + 1:]
                break
except Exception as ex:
    pass

try:
    for wordline in panline:
        xx = wordline.split()
        if [w for w in xx if re.search(numRE_str, w)]:
            pan = panline[panline.index(wordline) + 1]
            break
    pan = pan.replace(" ", "")
except Exception as ex:
    pass

# Making tuples of data
data = {'Name': name, 'Father Name': fname, 'Date of Birth': dob, 'PAN': pan}

# Writing data into JSON
# with open('../result/' + os.path.basename(sys.argv[1]).split('.')[0]
#           + '.json', 'w') as fp:
#     json.dump(data, fp)



'''
# Reading data back JSON(give correct path where JSON is stored)
with open('../result/'+sys.argv[1]+'.json', 'r') as f:
     ndata = json.load(f)
print "+++++++++++++++++++++++++++++++"
print(ndata['Name'])
print "-------------------------------"
print(ndata['Father Name'])
print "-------------------------------"
print(ndata['Date of Birth'])
print "-------------------------------"
print(ndata['PAN'])
print "-------------------------------"
#'''
