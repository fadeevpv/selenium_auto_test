from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link ="https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Кликаем кнопку для открытия второй страницы
    button1 = browser.find_element_by_xpath('//button[@type="submit"]')
    button1.click()

    # Выбираем  вторую открытую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
