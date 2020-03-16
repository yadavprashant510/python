import time

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

try:
    Options = webdriver.ChromeOptions()
    # fireFoxOptions.set_headless()
    driver: WebDriver = webdriver.Chrome(options = Options)
    url = "https://insight.eclerx.com"
    driver.get(url)
    alert = driver.switch_to_alert()
    time.sleep(2)
    alert.send_keys("prashant")
    print(driver.page_source)
finally:
    try:
        driver.close()
    except Exception as e:
        print(e)
