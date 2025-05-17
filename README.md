# ProductionDashboard
![DWH](/images/DWH.jpg)
**Настройка**
- Установить пути в файле .env  
   PATH_TO_XLSX = 'Путь куда грузим данные из источника.'  
   PATH_TO_CSV = 'Путь куда сохраняем обработанные данные. Готовы к загрузке в БД.'  
   URL = 'URL сайта.'  
   ODDO_LOGIN = 'Логин от Аккаунта Odoo.'  
   ODOO_PASSWORD = 'Пароль от Аккаунта Odoo.'  
- Установить путь загрузки данных в файле [task1](task1_raw_insert.sql)  
   COPY stage.raw_data (data) FROM '**Ваш путь**' WITH (FORMAT CSV, HEADER FALSE, DELIMITER ';', ENCODING 'utf-8');

**Схема работы ETL:** 
- Запуск [task1](download_dataset.py):
  Загрузка данных с сайта, очистка, логирование.
- Запуск [task2](task1_raw_insert.sql): 
  Загрузка raw_data в stage слой.  
- Запуск [task3](task2_core_insert.sql): 
  Загрузка в core слой. 
- Запуск [task4](task3_data_mart_insert.sql)
  Загрузка в data_mart слой.

 

