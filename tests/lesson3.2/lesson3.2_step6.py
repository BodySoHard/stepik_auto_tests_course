import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # нет ошибки
    assert abs(-42) == 42
    # есть ошибка
    # assert abs(-42) == -42
    # есть ошибка с описанием
    assert abs(-42) == -42, "Значение не положительное"

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
