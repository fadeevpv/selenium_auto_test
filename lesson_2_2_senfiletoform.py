from selenium import webdriver
import os
import time

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Заполняем поля
    input1 = browser.find_element_by_xpath('//input[@name="firstname"]')
    input1.send_keys("KTULXU")
    input2 = browser.find_element_by_xpath('//input[@name="lastname"]')
    input2.send_keys("Zaratustravich")
    input3 = browser.find_element_by_xpath('//input[@name="email"]')
    input3.send_keys("parampam@mail.ru")
    # Получаем путь к файлу расположенному в той же дирреткории с выполняемым скриптом
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добовляем к пути имя файла
    file_path = os.path.join(current_dir, 'importdata.txt')
    # находим кнопку для вложения файла
    element = browser.find_element_by_xpath('//input[@id="file"]')
    element.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@class="btn btn-primary"]')
    button.click()

finally:
    # проверяем что все ок
    time.sleep(20)
    # Закрываем окно
    browser.quit()