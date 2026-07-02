SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
On e.managerID =m.id 
WHERE e.salary > m.salary;