from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находи X
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text

    # прокручиваем страницу вниз
    browser.execute_script("window.scrollBy(0, 159);")

    # Считаем значения для ввода
    y = calc(x)

    # Находим поле для ввода ответ
    input1 = browser.find_element_by_id('answer')
    # В водим значение ответ
    input1.send_keys(y)

    # Выбираем чек бокс Я робот
    check1 = browser.find_element_by_id('robotCheckbox')
    check1.click()

    # Выбираем радиокнопку Роботы рулят
    check2 = browser.find_element_by_id('robotsRule')
    check2.click()

    # Находим и кликаем  кнопку и отправляем форму
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    # Проверяем что все ок
    time.sleep(5)

finally:

    # проверяем что все прошло удачно
    time.sleep(10)

    # Закрываем окно
    browser.quit()