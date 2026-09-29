CREATE DATABASE ecommerce;

USE ecommerce;

-- Users table
CREATE TABLE users (
id INT PRIMARY KEY,
name VARCHAR(50)

-- Products table
CREATE TABLE products (
id INT PRIMARY KEY,
name VARCHAR(100),
price DECIMAL(10, 2)

-- Orders table (foreign keys to users and products)
CREATE TABLE orders
id INT PRIMARY KEY,
user_id INT,
product_id INT,
order_date DATE,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (product_id) REFERENCES products(id)
