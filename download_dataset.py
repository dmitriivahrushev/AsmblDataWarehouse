import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv



URL = 'https://odoo.b4com.tech/web/login'


"""Импорт паролей для авторизации."""
load_dotenv()
LOGIN = os.getenv('ODDO_LOGIN')
PASSWORD = os.getenv('ODOO_PASSWORD')


"""Вход на сайт."""
driver = webdriver.Chrome()
driver.get(URL)
actions = ActionChains(driver)
time.sleep(2)

find_login = driver.find_element(By.ID, 'login')
find_password = driver.find_element(By.ID, 'password')
find_login.send_keys(LOGIN)
find_password.send_keys(PASSWORD)
time.sleep(2)


"""Скачать dataset.XLSX"""
driver.find_element(By.XPATH, '//button[.="Войти"]').click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, 'dropdown-toggle').click()
time.sleep(5)
driver.find_element(By.XPATH, '//a[.="Производство"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//span[.="Избранное"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//span[.="Выработка производства"]').click() 
time.sleep(5)
filter = driver.find_element(By.XPATH, '//span[.="Фильтры"]')
actions.move_to_element(filter).perform()
time.sleep(5)
driver.find_element(By.XPATH, '//span[.="Произведено за сегодня"]').click() 
time.sleep(5)
driver.find_element(By.XPATH, '//button[@class="btn btn-light o_switch_view o_pivot oi oi-view-pivot"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//button[@class="btn btn-secondary fa fa-download o_pivot_download"]').click()
time.sleep(20)


"""Сохрание файла в формате csv и пермещение в C:\Temp"""
