import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file_test.txt')

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname").send_keys('Anton')
    surname = browser.find_element(By.NAME, "lastname").send_keys('LLookin')
    email = browser.find_element(By.NAME, "email").send_keys('anton_lokkin@yandex.ru')

    file = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
