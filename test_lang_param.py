import time

from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket(browser):
    browser.get(link)

    assert browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    time.sleep(3)