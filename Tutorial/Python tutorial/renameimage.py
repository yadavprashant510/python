import os
# path = r"F:\Images\Clases"
# files = os.listdir(path)
# i = 1

# for image in files:
#     if str(image).endswith(".jpg"):
#         # print(image)
#         dest ="Classes "+str(i)+".jpg"
#         src = os.path.join(path,str(image))
#         os.rename(src,os.path.join(path,dest))
#         i += 1
# print("File rename successfully...")

path = r'F:\Download'
for folderName, subfolders, filenames in os.walk(path):
    os.rename(os.path.join(folderName),os.path.join(folderName.capitalize()))
    print('The current folder is = ' + folderName)

    for subfolder in subfolders:
        os.rename(os.path.join( folderName,subfolder),os.path.join(folderName,subfolder.capitalize()))
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        file2 = filename.capitalize()
        os.rename(os.path.join(folderName,subfolder,filename),
                os.path.join(folderName,subfolder,file2))
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
