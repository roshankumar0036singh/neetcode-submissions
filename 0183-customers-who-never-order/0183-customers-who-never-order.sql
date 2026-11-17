# Write your MySQL query statement below
select c1.name as Customers from Customers c1 left join orders o2 on c1.id=o2.customerId where o2.id is Null
