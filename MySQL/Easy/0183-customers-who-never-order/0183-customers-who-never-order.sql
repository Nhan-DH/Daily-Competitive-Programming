# Write your MySQL query statement below
Select Customers.name AS Customers from Customers
left join Orders ON Customers.id = Orders.customerID
where Orders.customerId IS NULL