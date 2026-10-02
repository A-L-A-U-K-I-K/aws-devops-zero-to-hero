USE ecommerce;

SELECT
	orders.id AS order_id,
	users.name AS user_name,
	products.name AS product_name,
	products.price,
	orders.order_date
FROM orders
JOIN users ON orders.user_id = users.id
JOIN products ON orders.product_id = products.id;