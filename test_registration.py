
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


    # Тестовая функция
 def test_registration(driver,wait):
       driver.get("https://victoretc.github.io/selenium_waits/")



   # Проверяем заголовок(С использованием Explict)
    epected_title = "Практика с ожиданиями в Selenium"
    title_element = wait.until(EC.visibility_of_element_located(By.XPATH, "/html/body/h1"))
    assert title_element.text == expected_title


   # Дожидаемся появления кнопки "Начать тестирование" (с использованием time.sleep())
    time.sleep(7)  # Подождать 3 секунды для демонстрации
    start_button = driver.find_element(By.XPATH, "///*[@id='startTest']")
    start_button.click()

   # Вводим логин и пароль
    login_input = driver.find_element(By.XPATH, "//*[@id='login']")
    login_input.send_keys("login")
    password_input = driver.find_element(By.XPATH, "//*[@id='password']")
    password_input.send_keys("password")

    # Устанавливаем флажок согласия с правилами
    agree_checkbox = driver.find_element(By.XPATH, "//*[@id='registrationForm']/label[3]")
    agree_checkbox.click()

    # Нажимаем кнопку "Зарегистрироваться"
    register_button = driver.find_element(By.XPATH, "//*[@id='register']")
    register_button.click()

    # Проверяем индикатор загрузки
    loading_indicator = wait.until(EC.visibility_of_element_located(By.XPATH, "//*[@id='loader']"))


    # Проверяем сообщение об успешной регистрации
    expected_success_message = "Вы успешно зарегистрированы!"
    success_message = wait.until(EC.visibility_of_element_located(By.XPATH, "//*[@id='successMessage']"))
    assert success_message.text == expected_success_message

