from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем Х
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    print(x)
    y = calc(x)
     # Находим нужные чек боксы и отмечаем
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn-default")
    button.click()

    # Проверяем загрузку страницы
    time.sleep(110)

finally:
    # Проверяем что все прошло удачно
    time.sleep(10)

    # Закрываем браузер
    browser.quit()