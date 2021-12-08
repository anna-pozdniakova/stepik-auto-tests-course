from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element=browser.find_element_by_css_selector('#price')
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y=calc(x)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()