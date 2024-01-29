import math
import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize( 'lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.implicitly_wait(20)
    browser.get(link)
    # Регистрация
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "ember33"))
    )
    button.click()
    input1 = browser.find_element(By.NAME, 'login')
    input1.send_keys("bodysohard@gmail.com")
    input2 = browser.find_element(By.NAME, 'password')
    input2.send_keys("Jek4.LS#f87PrHv")
    submit_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    submit_button.click()
    time.sleep(2)
    # Тест
    input3 = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']"))
    )
    input3.send_keys(str(math.log(int(time.time()))))

    send_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )

    send_button.click()

    text_elt = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    text = text_elt.text
    assert text == "Correct!"
