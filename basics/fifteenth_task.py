import time

from selenium import webdriver
from math import log, sin

from selenium.webdriver.common.by import By

def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit'")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = calc(browser.find_element(By.ID, "input_value").text)

    input = browser.find_element(By.CSS_SELECTOR, "input").send_keys(x)

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()