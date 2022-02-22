from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
# Прокрутим немного страничку
browser.execute_script("window.scrollBy(0, 500);")
# Говорим драйверу, что как только цена будет 100 то кликаем на  кнопку заказ
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
# Кликаем кнопку заказ как только цена будет 100
button = browser.find_element_by_xpath('//button[@id="book"]')
button.click()


# Берем значение X
x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
x = x_element.text

# Вычесляем Y
y = calc(x)

# Ищем поле и  водим значение Y
input1 = browser.find_element_by_xpath('//input[@id="answer"]')
input1.send_keys(y)

# Прокрутим немного страничку
browser.execute_script("window.scrollBy(0, 500);")

# Ищем  кнопку и отправляем заполнную форму
button1 = browser.find_element_by_xpath('//button[@id="solve"]')
button1.click()
# проверяем что все ок
time.sleep(10)
# закрываем окошки
browser.quit()