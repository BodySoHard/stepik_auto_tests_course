import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # вывести alert
    browser.execute_script("alert('Robots at work');")
    # изменить название вкладки
    browser.execute_script("document.title='Script executing';")
    # изменить название вкладки и вывести alert
    browser.execute_script("document.title='Script executing';alert('Robots at work');")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
