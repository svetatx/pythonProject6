from selenium.webdriver.common.by import By






# # Registration Page

title_element = (By.XPATH, "/html/body/h1")
start_button = (By.XPATH, "///*[@id='startTest']")
login_input = (By.XPATH, "//*[@id='login']")
password_input = (By.XPATH, "//*[@id='password']")
agree_checkbox = (By.XPATH, "//*[@id='registrationForm']/label[3]")
register_button = (By.XPATH, "//*[@id='register']")
loading_indicator = (By.XPATH, "//*[@id='loader']")
success_message = (By.XPATH, "//*[@id='successMessage']")