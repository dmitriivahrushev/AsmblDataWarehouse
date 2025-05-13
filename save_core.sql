CREATE SCHEMA IF NOT EXISTS core;

CREATE TABLE IF NOT EXISTS core.product_type (
   product_pn INTEGER PRIMARY KEY NOT NULL,
   name VARCHAR NOT NULL  
);
COMMENT ON TABLE core.product_type IS 'Виды продукта.';
COMMENT ON COLUMN core.product_type.product_pn IS 'PN Продукта.';
COMMENT ON COLUMN core.product_type.name IS 'Имя Продукта';

CREATE TABLE IF NOT EXISTS core.production (
    id INTEGER GENERATED ALWAYS AS IDENTITY NOT NULL,
    product_pn INTEGER NOT NULL,
    quantity INTEGER,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_pn FOREIGN KEY (product_pn) REFERENCES core.product_type (product_pn) ON DELETE RESTRICT,
    CONSTRAINT pk_id PRIMARY KEY (id)
);
COMMENT ON TABLE core.production IS 'Произведенная продукция.';
COMMENT ON COLUMN core.production.id IS 'Уникальный идентификатор кортежа.';
COMMENT ON COLUMN core.production.product_pn IS 'PN Продукта.';
COMMENT ON COLUMN core.production.quantity IS 'Произведенное количество.';
COMMENT ON COLUMN core.production.date IS 'Время производства продукта.';

--Наполнение таблиц--
SELECT DISTINCT
       REPLACE(SPLIT_PART(DATA, ']', 1), '[', '') AS pn, 
       SUBSTRING(data from '](.*?);') AS name
FROM stage.raw_data
WHERE data LIKE '%[%';