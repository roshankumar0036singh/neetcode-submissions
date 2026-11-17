CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  IF N<1 THEN
    RETURN;
  END IF;
  RETURN QUERY (
    SELECT DISTINCT Employee.salary from Employee order by Employee.salary desc limit 1 offset N-1
    
    
      
  );
END;
$$ LANGUAGE plpgsql;