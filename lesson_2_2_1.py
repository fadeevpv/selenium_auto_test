from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select




try:
    link ="http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем x
    x_element = browser.find_element_by_xpath('//span[@id="num1"]')
    x = x_element.text
    print(x)

    # Вычисляем y
    y_element = browser.find_element_by_xpath('//span[@id="num2"]')
    y = y_element.text
    print(y)

    # Сумму значений x и y
    z = (int(x) + int(y))
    print(z)

    # Раскрываем выпадайку
    select = Select(browser.find_element_by_xpath('//select[@id="dropdown"]'))
    # Выбираем из выпадайки сумму значени x + y
    select.select_by_value(value=str(z))

    # Кликаем по кнопке submit
    button = browser.find_element_by_class_name('btn-default').click()




finally:
    # Проверяем что все прошло удачно
    time.sleep(6)

    # Закрываем окно
    browser.quit()
