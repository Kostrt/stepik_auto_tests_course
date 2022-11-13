from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
         )

    # клик кнопку "бронь"
    button = browser.find_element(By.ID, "book")
    button.click()

        # Ваш код, который заполняет обязательные поля
    attrinute = browser.find_element(By.ID, "input_value")
    attrinute = attrinute.text
    y = calc(attrinute)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # клик кнопку "submit"
    button = browser.find_element(By.ID, "solve")
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