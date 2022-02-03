from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://snt-stroitel.ru/")

driver.implicitly_wait(10)

# кнопка пообщаемся на форуме на главной странице
driver.get("https://snt-stroitel.ru/")
button_forum = driver.find_element(By.XPATH, '//*[@id="slider"]/div/div[2]/div/div/div/a[1]').click()

driver.implicitly_wait(10)

# кнопка новости на главной странице
driver.get("https://snt-stroitel.ru/")
button_news = driver.find_element(By.XPATH, '//*[@id="slider"]/div/div[2]/div/div/div/a[2]').click()

driver.implicitly_wait(10)

# последние статьи на сайте
driver.get("https://snt-stroitel.ru/")
ads = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[1]/a').click() # объявления на заборах
# '//*[@id="recent-posts-3"]/ul/li[1]/a'

driver.implicitly_wait(10)

driver.get("https://snt-stroitel.ru/")
test_access = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[2]/a').click() #тестируем разграничение доступа

driver.implicitly_wait(10)

driver.get("https://snt-stroitel.ru/")
sites_snt = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[3]/a').click() # сайты других снт

driver.implicitly_wait(10)

driver.get("https://snt-stroitel.ru/")
sait_position = driver.find_element(By.XPATH,'//*[@id="recent-posts-3"]/ul/li[4]/a').click() #сайт и отношение к нему

driver.implicitly_wait(10)

driver.get("https://snt-stroitel.ru/")
how_to_login = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[5]/a').click() #как зарегистрироваться

driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
restricting_access = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[6]/a').click() #ограничение доступа на сайт для посторонних

driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
foto_gallery = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[7]/a').click() # прикрутил на сайт галерею с фото

driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
meeting_video = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[8]/a').click() # видео с собрания

driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
privet_vsem = driver.find_element(By.XPATH, '//*[@id="recent-posts-3"]/ul/li[9]/a').click() # привет всем

#заголовок сайта на главной странице
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
resident_sait = driver.find_element(By.XPATH, '//*[@id="masthead"]/div[1]/div/div/div/div/h1/a').click()

#кнопки на зеленой полосе вверху
#форум
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
forum = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[1]/a').click()

#новости
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
news = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[2]/a').click()

#о снт
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
about_snt =  driver.find_element(By.XPATH,'//*[@id="primary-menu"]/li[3]/a').click()

#о снт - контакты
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
about_snt =  driver.find_element(By.XPATH,'//*[@id="primary-menu"]/li[3]/a')
ActionChains(driver).move_to_element(about_snt).perform()
about_snt_contacts = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[3]/ul/li[1]/a').click()


#о снт - галерея
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
about_snt =  driver.find_element(By.XPATH,'//*[@id="primary-menu"]/li[3]/a')
ActionChains(driver).move_to_element(about_snt).perform()
about_snt_gallery = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[3]/ul/li[2]/a').click()

#войти
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
entrance = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[4]/a').click()

#зарегистрироваться
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
registered = driver.find_element(By.XPATH, '//*[@id="primary-menu"]/li[5]/a').click()

# кнопка поиска на главной странице
driver.implicitly_wait(10)
driver.get("https://snt-stroitel.ru/")
search_button = driver.find_element(By.ID, "search-btn").click()

driver.implicitly_wait(10)

search_field = driver.find_element(By.XPATH, '//*[@id="masthead"]/div[3]/div/div/div/form/label/input')
search_field.send_keys("форум")
search_field.send_keys(Keys.ENTER)

driver.quit()