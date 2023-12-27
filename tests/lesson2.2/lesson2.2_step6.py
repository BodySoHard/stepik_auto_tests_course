import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(h):
        return str(math.log(abs(12 * math.sin(int(h)))))

    # Считать значение для переменной x
    robots_radio = browser.find_element(By.ID, "input_value")
    x = robots_radio.text
    # Посчитать математическую функцию от x
    y = calc(x)
    # Проскроллить страницу вниз
    input1 = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    # Ввести ответ в текстовое поле
    input1.send_keys(y)
    # Выбрать checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    # Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    # Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
