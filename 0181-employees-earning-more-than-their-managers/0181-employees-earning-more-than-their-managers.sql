# Write your MySQL query statement below
SELECT e.name as Employee from Employee e inner join employee m on e.managerId=m.id where e.salary>m.salary;
