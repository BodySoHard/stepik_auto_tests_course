from selenium import webdriver

try:
    browser = webdriver.Chrome()
    # нет ошибки
    assert abs(-42) == 42
    # есть ошибка
    # assert abs(-42) == -42
    # Форматирование строк с помощью str.format
    print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
    # Форматирование строк с помощью f-strings
    str1 = "one"
    str2 = "two"
    str3 = "three"
    print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

    #
    actual_result = "abrakadabra"
    print(f"Wrong text, got {actual_result}, something wrong")

    # составные сообщения об ошибках и поиск подстроки
    s = 'My Name is Julia'

    if 'Name' in s:
        print('Substring found')

    index = s.find('Name')
    if index != -1:
        print(f'Substring found at index {index}')

    # есть ошибка с описанием
    assert abs(-42) == -42, "Значение не положительное"

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
