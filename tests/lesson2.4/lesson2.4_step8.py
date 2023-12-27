import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    def calc(h):
        return str(math.log(abs(12 * math.sin(int(h)))))

    # Дождаться, когда цена дома уменьшится до $100
    img = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    # Нажать на кнопку "Book"
    button = browser.find_element(By.ID, "book")
    button.click()
    # Считать значение для переменной x
    robots_radio = browser.find_element(By.ID, "input_value")
    x = robots_radio.text
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    # Нажать на кнопку "Submit"
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
