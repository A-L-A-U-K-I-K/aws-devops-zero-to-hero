USE ecommerce;

Insert users
INSERT INTO users VALUES (1, 'John Doe');
INSERT INTO users VALUES (2, 'Jane Smith');

-- Insert products
INSERT INTO products VALUES (1, 'Wireless Mouse', 25.99);
INSERT INTO products VALUES (2, 'Mechanical Keyboard', 79.99);

-- Insert orders
INSERT INTO orders VALUES (1, 1, 2, '2025-03-01'); -- John orders Keyboard
INSERT INTO orders VALUES (2, 2, 1, '2025-03-02'); -- Jane orders Mouse