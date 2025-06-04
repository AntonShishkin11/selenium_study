import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def calc(x):
    return str(log(abs(12*sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)

    WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x = calc(browser.find_element(By.ID, "input_value").text)

    input = browser.find_element(By.CSS_SELECTOR, "input").send_keys(x)

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
