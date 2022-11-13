from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

# input field
    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Art")
    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("Ko")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("Art@ko.tu")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'input_test.txt')           # добавляем к этому пути имя файла 
    
    in_file = browser.find_element(By.ID, "file")
    in_file.send_keys(file_path)

    # button
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

