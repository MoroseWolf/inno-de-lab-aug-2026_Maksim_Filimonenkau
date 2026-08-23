-- Задание 1: Создать нового пользователя PostgreSQL (роль) с именем hr_user
CREATE USER hr_user WITH PASSWORD '1111'

-- Задание 2: дать доступ к SELECT в Employees
GRANT
SELECT
	ON
	Employees TO hr_user
	
-- Задание 3: проверить работу доступов
SELECT
	*
FROM
	Employees;
-- работает

-- Задание 4: добавить права INSERT, UPDATE
GRANT
UPDATE
	,
	INSERT
	ON
	Employees TO hr_user

-- Задание 5: проверить работу изменений
UPDATE
	employees
SET
	Salary = 65001.00
WHERE
	FirstName = 'Alice'
	AND Lastname = 'Smith'
    
INSERT
	INTO
	Employees (FirstName,
	LastName,
	Department,
	Salary)
VALUES 
('Test',
'Testovich',
'HR',
777.00)
