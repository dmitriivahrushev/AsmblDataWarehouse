CREATE SCHEMA IF NOT EXISTS stage;

DROP TABLE IF EXISTS stage.raw_data ;
CREATE TABLE stage.raw_data (
   data TEXT,
   data_load TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE stage.raw_data IS 'Сырые данные из источника.';
COMMENT ON COLUMN stage.raw_data.data IS 'Поле с данными.';
COMMENT ON COLUMN stage.raw_data.data_load IS 'Время загрузки.';

COPY stage.raw_data (data) FROM 'C:\Temp\raw_data.csv' WITH (FORMAT CSV, HEADER FALSE, DELIMITER ',');