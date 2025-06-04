import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем в Pytest параметр --browser_name, теперь при запуске тестов мы можем прописать pytest -s -v --browser_name=chrome
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # Добавляем в Pytest параметр --langugae для выбора языка, на котором будет запущен сайт
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language")


@pytest.fixture(scope="function")
# С помощью этой фикстуры Pytest поймет какой браузер запускать pytest -s -v --browser_name=firefox test_parser.py
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()

