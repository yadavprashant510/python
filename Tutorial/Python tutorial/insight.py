import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = r"F:/Python/Tutorial"


def csv_writer(Date, in_time, out_time):
    with open(os.path.join(path, 'working.csv'), mode = 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([Date, in_time, out_time])


def overwrite_csv():
    with open('working.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        header = ["Date", "In Time", "Out Time"]
        writer.writerow(header)


def date_picker(date):
    driver.find_element_by_id("AttendanceDate").clear()
    driver.find_element_by_id("AttendanceDate").click()
    element = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody')
    rows = element.find_elements_by_tag_name("tr")
    columns = element.find_elements_by_tag_name("td")
    for cell in columns:
        if cell.text == str(date):
            cell.find_element_by_link_text(str(date)).click()
            return date


def refresh_page():
    reports_menu = driver.find_element_by_xpath('//a[contains(text(),"Report")]').click()
    emp_swipe_info = driver.find_element_by_xpath('//img[@alt="Employee Swipe Info"]').click()
    emp_name = wait.until(EC.presence_of_element_located((By.XPATH,
                                                          '//input[@class="ui-autocomplete-input"]'))).send_keys(
        "35762")
    return


options = webdriver.ChromeOptions()
options._binary_location = "D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options = options)
wait = WebDriverWait(driver, 10)
url = driver.get("https://prashant.yadav:Eclerx@123@insight.eclerx.com")
# url2 = driver.get("https://insight.eclerx.com")
time.sleep(1)
driver.maximize_window()
driver.implicitly_wait(15)
action_chain = ActionChains(driver)
menu = driver.find_element_by_xpath('//a[@class = "un-menu"]').click()
leave_attendance = driver.find_element_by_xpath('//a[contains(text(),"Leave & Attendance")]').click()
refresh_page()
no_of_date = [9, 11, 12, 13]
overwrite_csv()
try:
    for date in no_of_date:
        date_picker(date)
        search_btn = driver.find_element_by_xpath('//div[3]/a[contains(text(),"Search")]').click()
        time.sleep(4)
        # try:
        #     if driver.find_element_by_xpath("//div[contains(text(),'No data available')]").is_displayed():
        #         print("No Data Found.")
        #         continue
        # except Exception as e:
        #     print(e)
        # time.sleep(5)
        wait_time = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="GridView1"]\
                                                        /tbody/tr[2]/td[11]/div')))
        driver.execute_script("arguments[0].scrollIntoView();", wait_time)
        # action_chain.drag_and_drop_by_offset(hbar,217,0).perform()
        In_time = driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[2]/td[11]/div').text
        Out_time = driver.find_element_by_xpath('//*[@id="GridView1"]/tbody/tr[3]/td[11]').text
        D = driver.find_element_by_xpath('//tr[@class="GridviewScrollItem"]/td[10]/div').text
        driver.execute_script("window.scrollBy(0,-200)")
        csv_writer(D, In_time, Out_time)
        if (In_time != "") and (Out_time != ""):
            print(f"Date:{D}", end = "  ")
            print(f"In-Time = {In_time}", end = " ")
            print(f"Out-Time = {Out_time}", end = " ")
            print()
        else:
            print("Data not found.")
except Exception as e:
    print(e)
driver.close()
