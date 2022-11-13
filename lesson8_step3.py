from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
import math

#def calc(x, y):
 # return str(math.(x + y))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # find atribute
    attrinute1 = browser.find_element(By.ID, "num1")
    attrinute2 = browser.find_element(By.ID, "num2")
   # answer = calc(attrinute1, attrinute2)
    answer = str(int(attrinute1.text) + int(attrinute2.text))
    print(answer)

    # отчемаем chekbox и radiobutten
    #select = Select(browser.find_element(By.ID, "dropdown"))
    #select.select_by_value(answer)
    option1 = browser.find_element(By.ID, "dropdown")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='" + answer + "']")
    option2.click()

   


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    #