import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    # проскроллить до кнопки button
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # проскроллить страницу на 100 пикселей
    # browser.execute_script("window.scrollBy(0, 100);")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
