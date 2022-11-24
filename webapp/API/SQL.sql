CREATE TABLE products
(
    id serial PRIMARY KEY,
    product_name varchar(150) NOT NULL
);

CREATE TABLE categories
(
    id serial PRIMARY KEY,
    category_name varchar(150) NOT NULL
);

CREATE TABLE products_categories
(
    product_id int REFERENCES products(id),
    category_id int REFERENCES categories(id),
    CONSTRAINT products_categories_pk PRIMARY KEY (product_id, category_id)
);

INSERT INTO products (product_name) VALUES ('apple');

INSERT INTO products (product_name) VALUES ('juice');

INSERT INTO products (product_name) VALUES ('bread');

INSERT INTO products (product_name) VALUES ('chocolate');

INSERT INTO products (product_name) VALUES ('cookie');

INSERT INTO products (product_name) VALUES ('cake');

INSERT INTO categories (category_name) VALUES ('fruit');

INSERT INTO categories (category_name) VALUES ('confectionery');

INSERT INTO categories (category_name) VALUES ('bakery');

INSERT INTO categories (category_name) VALUES ('soft drinks');

INSERT INTO products_categories VALUES (1, 1), (2, 4), (3, 3), (4, 2), (5, 2); 

SELECT products.product_name, categories.category_name
FROM products
LEFT JOIN products_categories
ON products_categories.product_id=products.id
LEFT JOIN categories
ON categories.id=products_categories.category_id;








