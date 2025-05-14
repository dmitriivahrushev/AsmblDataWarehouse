CREATE SCHEMA IF NOT EXISTS core;


CREATE TABLE IF NOT EXISTS core.product_type (
   product_id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
   product_name VARCHAR NOT NULL, 
   product_pn VARCHAR NOT NULL,
   CONSTRAINT pk_product_id PRIMARY KEY (product_id)
);
COMMENT ON TABLE core.product_type IS 'Виды продукта.';
COMMENT ON COLUMN core.product_type.product_id IS 'ID Продукта.';
COMMENT ON COLUMN core.product_type.product_name IS 'Имя Продукта';
COMMENT ON COLUMN core.product_type.product_pn IS 'PN Продукта.';

CREATE TABLE IF NOT EXISTS core.production (
    id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
    product_id INTEGER NOT NULL,
    product_name VARCHAR NOT NULL,
    quantity INTEGER,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES core.product_type (product_id) ON DELETE RESTRICT,
    CONSTRAINT pk_id PRIMARY KEY (id)
);
COMMENT ON TABLE core.production IS 'Произведенная продукция.';
COMMENT ON COLUMN core.production.id IS 'Уникальный идентификатор кортежа.';
COMMENT ON COLUMN core.production.product_id IS 'ID Продукта.';
COMMENT ON COLUMN core.production.product_name IS 'Имя Продукта.';
COMMENT ON COLUMN core.production.quantity IS 'Произведенное количество.';
COMMENT ON COLUMN core.production.date IS 'Время производства продукта.';


INSERT INTO core.product_type (product_name, product_pn)
SELECT DISTINCT
       SUBSTRING(data from '](.*?);')::VARCHAR AS product_name,
       REPLACE(SPLIT_PART(DATA, ']', 1), '[', '')::VARCHAR AS product_pn  
FROM stage.raw_data
WHERE data LIKE '%[%';


--ДЕБАГ
SELECT 
    SUBSTRING(data from '](.*?);')::VARCHAR AS product_name,
	REPLACE(SPLIT_PART(DATA, ';', 2), '[', '')::INT AS quantity
FROM stage.raw_data AS src
LEFT JOIN core.product_type AS pt ON SUBSTRING(src.data from '](.*?);')::VARCHAR = pt.product_name AND REPLACE(SPLIT_PART(src.DATA, ']', 1), '[', '')::VARCHAR = pt.product_pn
WHERE data LIKE '%[%';
--