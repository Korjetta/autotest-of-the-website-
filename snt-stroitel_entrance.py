from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.maximize_window()

driver.get("https://snt-stroitel.ru/")
driver.implicitly_wait(10)

#войти
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
entrance = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[4]/a').click()

#поле ввода "логин или e-mail"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username-240"]'))).send_keys("test_user_00@internet.ru")

#поле ввода "пароль"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user_password-240"]'))).send_keys("Pp123456")
driver.implicitly_wait(10)



