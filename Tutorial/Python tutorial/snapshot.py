import pyscreenshot as ImageGrab
import os, sys
import webbrowser
import openpyxl as xl
if __name__ == '__main__':
    # grab fullscreen
    # explorer = webbrowser.open('explorer', "F:\\PRICE REFRESH\\AE\\OFFER\\2019\\12\\"
    #                                        "HOURLY\\2019-12-12")
    webbrowser.open("F:\\PRICE REFRESH\\AE\\OFFER\\2019\\12\\"
                    "HOURLY\\2019-12-12")
    # folder = os.startfile()
    # open_dir = explorer()
    im = ImageGrab.grab()

    # save image file
    user_choice = input('Do you want to take  screenshot? (Y/N)- ')
    # user_choice = "y"
    if user_choice.lower() == 'n':
        sys.exit()

    im.save('screenshot.jpeg')

    # show image in a window
    im.show()
