import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

# получить значение из атрибута valuex
    robots_radio = browser.find_element(By.ID, "num1")
    x = robots_radio.text #получить значение в элементе
    robots_radio2 = browser.find_element(By.ID, "num2")
    y = robots_radio2.text #получить значение в элементе
    z = str(str(int(x)+int(y)))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
