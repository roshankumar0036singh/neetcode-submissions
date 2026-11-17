# Write your MySQL query statement below
select a.player_id , a.event_date as first_login from Activity a  left join Activity e  on a.player_id=e.player_id and a.event_date>e.event_date
where e.player_id is Null;
