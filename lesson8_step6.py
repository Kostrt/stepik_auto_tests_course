from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    attrinute = browser.find_element(By.ID, "input_value")
    attrinute = attrinute.text
    y = calc(attrinute)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # отчемаем chekbox и radiobutten
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #