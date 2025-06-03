import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = 'https://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    el_x = browser.find_element(By.ID, "treasure")
    x = int(el_x.get_attribute("valuex"))

    ans = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "input")
    input.send_keys(ans)

    checkbox = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
