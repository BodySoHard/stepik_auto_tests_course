import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from selenium.webdriver.support.select import Select

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("https://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
