import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = calc(browser.find_element(By.ID, "input_value").text)

    input = browser.find_element(By.CSS_SELECTOR, "input").send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()




