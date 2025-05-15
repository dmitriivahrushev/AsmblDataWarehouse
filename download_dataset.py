import time
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from openpyxl import load_workbook

   
def load_dataset():
    """Импорт паролей для авторизации."""
    URL = 'https://odoo.b4com.tech/web/login'
    LOGIN = os.getenv('ODDO_LOGIN')
    PASSWORD = os.getenv('ODOO_PASSWORD')

    """Скачать dataset.XLSX"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    actions = ActionChains(driver)
    time.sleep(2)

    find_login = driver.find_element(By.ID, 'login')
    find_password = driver.find_element(By.ID, 'password')
    find_login.send_keys(LOGIN)
    find_password.send_keys(PASSWORD)
    time.sleep(2)

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



def transform_file():
    """Сохрание файла в формате csv и пермещение в C:\Temp"""
    PATH_TO_XLSX = 'C:\\Users\\w3bfr\\Downloads'
    PATH_TO_CSV = 'C:\\Temp\\raw_data.csv'  
    files = os.listdir(PATH_TO_XLSX)
    for file in files:
        if file.endswith('.xlsx'):
            book = load_workbook(os.path.join(PATH_TO_XLSX, file))
            sheet = book.active
            range_row = len(sheet['A'])
            continue

# Ошибка при загрузке файла в Postgres ругается на 3 строку.
    with open(PATH_TO_CSV, 'a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        for i in range(1, range_row):
            raw_data_col1 = f'{sheet['A' + str(i)].value}'
            raw_data_col2 = f'{sheet['B' + str(i)].value}'
            clear_col1 = raw_data_col1.strip()
            clear_col2 = raw_data_col2.strip()           
            if '[' not in clear_col1:
                continue
            elif ',' in clear_col1:
               del_comma = clear_col1.replace(',', '')
               writer.writerow([del_comma, clear_col2])
            else:
                writer.writerow([clear_col1, clear_col2])

   
            
        
    

if __name__=="__main__":
    load_dotenv()
    #load_dataset()
    transform_file()
    