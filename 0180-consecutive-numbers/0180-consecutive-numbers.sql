-- Write your PostgreSQL query statement below
with consecutivecheck As(
    select num,
    lag(num,1) over (order by id) as prev_num,
    lead(num,1) over (order by id ) as next_num
    from Logs
)
select distinct num as ConsecutiveNums
from consecutivecheck 
where num=prev_num and num=next_num;
