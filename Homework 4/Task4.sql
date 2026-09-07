-- Задание 1:  Увеличить Salary всех сотрудников в отделе 'HR' на 10%
UPDATE
	Employees
SET
	salary = salary + 0.1 * salary
WHERE
	department = 'HR'
	
-- Задание 2: Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'. 
UPDATE
	employees
SET
	Department = 'Senior IT'
WHERE
	salary > 70000.00
	
-- Задание 3: Удалить всех сотрудников, которые не назначены ни на один проект в таблице EmployeeProjects. 
DELETE
FROM
	employees AS e
WHERE
	NOT EXISTS (
	SELECT
		1
	FROM
		EmployeeProjects AS ep
	WHERE
		ep.employeeid = e.employeeid)
		
-- Задание 4: В рамках одной транзакции, вставить новый проект и назначить на него двух существующих сотрудников 
--с определенным количеством HoursWorked в EmployeeProjects.
BEGIN;

WITH new_project AS (
INSERT
	INTO
		Projects (ProjectName,
		Budget,
		StartDate,
		EndDate)
	VALUES ('Golang microservices',
	350000,
	'2026-08-01',
	'2027-03-31')
	RETURNING projectid
)

INSERT
	INTO
	employeeprojects (employeeid,
	projectid,
	hoursworked)
SELECT
	t.employeeid,
	np.projectid,
	t.hoursworked
FROM
	new_project AS np
CROSS JOIN (
VALUES (1,
50),
(3,
50)) AS t(employeeid, hoursworked);

COMMIT;
