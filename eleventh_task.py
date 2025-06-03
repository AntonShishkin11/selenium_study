import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    ans = num1 + num2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(ans))

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


