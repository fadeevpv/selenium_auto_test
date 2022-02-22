from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Кликаем по кнокпе для вывода алерта
    call_alt = browser.find_element_by_xpath('//button[@type="submit"]')
    call_alt.click()

    # Переключаемся на окно Алерт и подтверждаем переход
    confirm = browser.switch_to_alert()
    confirm.accept()

    # Находим число переменной
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
    # Вычесляем значение Y от X
    y = calc(x)
    # Заполняем форму переменной Y
    input1 = browser.find_element_by_xpath('//input[@id="answer"]')
    input1.send_keys(y)

    # отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@class="btn btn-primary"]')
    button.click()


finally:
    time.sleep(10)
    browser.quit()