import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(log(abs(12*sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)

    x = calc(int(browser.find_element(By.ID, "input_value").text))

    input = browser.find_element(By.CSS_SELECTOR, "input")
    input.send_keys(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
