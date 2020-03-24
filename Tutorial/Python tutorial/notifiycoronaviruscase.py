import requests
from bs4 import BeautifulSoup
from plyer import notification


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"F:\Python\Tutorial\coronavirus.ico",
        timeout = 10  # seconds
    )


if __name__ == '__main__':
    # notifyMe('Prashant', "Lets stop the spread of coronavirus.")
    url = "https://www.mohfw.gov.in/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    myDataStr = ''
    state = ['Maharashtra', 'Uttar Pradesh', 'Bihar']
    for tr in soup.find_all(class_ = "table-responsive")[7].find_all('tr')[1:]:
        # print(tr.get_text())
        myDataStr += tr.get_text()
    # print("my Data string :", format(myDatastr.split("\n\n")))
    item_list = myDataStr[1:].split("\n\n")
    for item in item_list[0:23]:
        data_list = item.split("\n")
        if data_list[1] in state:
            nTitle = 'Cases of Covid-19'
            nText = f"State : {data_list[1]}\nIndian : {data_list[2]} & Foreign :{data_list[3]}\n" \
                    f"Cured : {data_list[4]}\nDeaths : {data_list[5]} "
            notifyMe(nTitle, nText)
