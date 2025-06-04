import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.parametrize("login, password", [
#     ('annnt9na@yandex.ru', '2131F587j8-')
# ])
@pytest.mark.parametrize('link', [
    ('https://stepik.org/lesson/236895/step/1'),
    ('https://stepik.org/lesson/236896/step/1'),
    ('https://stepik.org/lesson/236897/step/1'),
    ('https://stepik.org/lesson/236898/step/1'),
    ('https://stepik.org/lesson/236899/step/1'),
    ('https://stepik.org/lesson/236903/step/1'),
    ('https://stepik.org/lesson/236904/step/1'),
    ('https://stepik.org/lesson/236905/step/1)')
])
def test_stepik_reg(browser, link):
    browser.get(link)

    wait = WebDriverWait(browser, 10)

    # Ждём и кликаем кнопку логина
    button_log = wait.until(EC.element_to_be_clickable((By.ID, 'ember479')))
    button_log.click()

    # Ждём, пока появятся поля для ввода логина и пароля и вводим данные
    email_input = wait.until(EC.visibility_of_element_located((By.ID, 'id_login_email')))
    email_input.send_keys('annnt9na@yandex.ru')

    password_input = wait.until(EC.visibility_of_element_located((By.ID, 'id_login_password')))
    password_input.send_keys('2131F587j8-')

    # Ждём и кликаем кнопку submit
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    time.sleep(3)

    # Ждём появления textarea и вводим ответ
    textarea = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea')))
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)

    # Ждём и кликаем кнопку отправки решения
    button_ans = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button_ans.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))

    result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    print(result)
    waiting_res = 'Correct!'
    assert str(result.strip()) == waiting_res







