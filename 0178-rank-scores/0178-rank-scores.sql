-- Write your PostgreSQL query statement below
select  Scores.score, Dense_Rank() over (order by Scores.score desc) as rank from Scores;

