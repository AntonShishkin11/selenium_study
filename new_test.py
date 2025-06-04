from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option, как указано в примере ниже:
#
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
# browser = webdriver.Chrome(options=options)
# Для Firefox объявление нужного языка будет выглядеть немного иначе:
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", user_language)
# browser = webdriver.Firefox(firefox_profile=fp)

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")