import time
from selenium import webdriver
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()

drive.get("https://www.songsterr.com/a/wsa/nirvana-lithium-tab-s34")

while True:
    try:
        but = drive.find_element(By.XPATH, '//a[text()="continue with interruptions"]')
        but.click()
        print("CLICKED")
    except:
        pass
    finally:
        time.sleep(0.01)
