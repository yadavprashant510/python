import os, webbrowser
from os.path import join
import shutil
from datetime import date
import pyscreenshot as image_grab
from tqdm import tqdm,trange


def get_report_time(file):
    file_name = get_file_name(file)
    report_time = file_name.rsplit("_")[-1]
    return report_time


def take_screenshot():
    # specific_folder = webbrowser.open('explorer')
    os.startfile(destn)
    image = image_grab.grab()
    image_saving_add = join(source_address, "Snapshot")
    file_name = get_file_name(file)
    if not os.path.exists(image_saving_add):
        os.mkdir(image_saving_add)
    image.save(join(image_saving_add, file_name+".jpeg"))
    # Image.show()


def get_file_name(file):
    name = file.replace(".xlsx", "")
    return name


def destination(address, file):
    if "uae" in file:
        address = join(address, "AE")
    elif "egy" in file:
        address = join(address, "EG")
    elif "ksa" in file:
        address = join(address, "SA")

    if "offer" in file:
        address = join(address, "OFFER")
    else:
        address = join(address, "PRICING")

    month = date.today().strftime("%m")

    # month_in_req_format = month.strftime("%B %Y")
    # address = join(address, str(month_in_req_format))
    date_format = date.today().strftime("%Y-%m-%d")
    address = join(address, str(date.today().year), str(month), "HOURLY", str(date_format))
    # address = join(address, str(date_format))
    # address = join(address, get_report_time(file))
    # address = join(address,"Output")
    return address


if __name__ == '__main__':
    source_address = "E:\Output"
    print("Source Address: "+source_address)
    dest = "F:\PRICE REFRESH"
    no_of_files = os.listdir(source_address)
    print("No of file for transfer: "+str(len(no_of_files)))

    for file in no_of_files:
        if str(file).endswith(".xlsx"):
            source = join(source_address, str(file))
            destn = destination(dest, file.lower())

            if not os.path.exists(destn):
                    os.makedirs(destn)
                    print("Directory: "+str(destn)+" created.")
            else:
                print("Directory: "+str(destn)+" already exist.")
        else:
            continue
        print(f"Processing {file}")
        shutil.copy2(source, destn)
        print(f"Completed..{file}")
        if get_report_time(file) == "1430":
            pass
            # take_screenshot()
        else:
            pass

    print("Files transferred successfully")






