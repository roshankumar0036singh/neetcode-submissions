# Write your MySQL query statement below
WITH RankedSalaries AS (select d.name as Department, e.name as Employee ,e.salary as Salary, Dense_Rank() over (partition by d.id order by e.salary desc) as rnk from employee e 
join department d on e.departmentid=d.id)
select Department ,Employee , Salary from RankedSalaries where rnk=1;
