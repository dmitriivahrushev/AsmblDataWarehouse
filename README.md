# AsmblDataWarehouse
![DWH](/images/DWH.jpg)
Проект ProductionDashboard представляет собой решение, которое позволяет извлекать, трансформировать, загружать данные в базу данных и визуализировать их.

### 🔧 Используемые инструменты.  
- **Airflow** - оркестрация ETL процессов.   
- **Odoo** - источник данных.  
- **Python** - инструмент для трансформации.  
- **SQL** - инструмент для загрузки данных.  
- **PosgreSQL** - база данных.  
- **Здесь будет визуализация** - ???.  
- **Docker-compose** - для облегчения развертывания сервисов.   

### 📁 Структура проекта

```
.
├── dags/                # DAG.
├── images/              # Изображения.
├── tmp_data/            # Хранение xlsx и csv файлов.
├──.gitignore/           # Файлы, игнорируемые Git-ом.
├── docker-compose.yaml/ # Плагины Airflow.
├── README.md/           # Информация о проекте.
└──  requirements.txt/   # Зависимости проекта.
```

### 🔨 Настройка
- Клонируем репозиторий.
- Поднимаем сервисы с помощю [docker-compose](docker-compose.yaml)
~~~
docker compose up
~~~
- В браузере переходим на http://localhost:8080
- Вводим логин и пароль (airflow, airflow)
- Настриваем коннектор.  
  Conn Id: postgres_dwh  
  Conn Type: postgres   
  Host: postgres_dwh    
  Port: 5432 
- В папке tmp_data лежит [dataset](/tmp_data/raw_data%20—%20копия.xlsx)
- Готово, теперь можно выставлять нужное время запуска DAG и база данных будет напоняться.
- Что бы подключиться к postgres:15  
  POSTGRES_USER: admin  
  POSTGRES_PASSWORD: admin  
  POSTGRES_DB: dwh_db  
  ports: 5433:5432  
  

### 📚 Схема работы ETL: 
![DAGS](/images/tasks.jpg)

  1️⃣Запуск [transform_file](dags/transform_file.py): Загрузка данных с сайта, очистка, логирование.  
  2️⃣Запуск [insert_stage](dags/insert_stage.py): Загрузка raw_data в stage слой.    
  3️⃣Запуск [insert_core](dags/insert_core.py): Загрузка в core слой.  
  4️⃣Запуск [insert_data_mart](dags/insert_data_mart.py): Загрузка в data_mart слой.

 

