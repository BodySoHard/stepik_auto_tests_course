import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Принять alert
    alert = browser.switch_to.alert
    alert.accept()

    # получить текст из alert
    alert = browser.switch_to.alert
    alert_text = alert.text

    # Нажать на ОК
    confirm = browser.switch_to.alert
    confirm.accept()

    # Нажать на Отмена
    confirm = browser.switch_to.alert
    confirm.dismiss()

    # Ввести текст и нажать на ОК
    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
