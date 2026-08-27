-- Задание 1: Функция: Создать функцию PostgreSQL с именем CalculateAnnualBonus, которая принимает employee_id и Salary 
-- в качестве входных данных и возвращает рассчитанную сумму бонуса (10 % от Salary) для этого сотрудника. 
-- Используйте PL/pgSQL для тела функции. 
CREATE OR REPLACE
FUNCTION CalculateAnnualBonus(
employee_id INTEGER,
salary numeric
)
RETURNS numeric
LANGUAGE PLpgSQL
AS $$
BEGIN
	RETURN salary * 0.1;
END;
$$;

-- Задание 2:Использовать эту функцию в операторе SELECT, чтобы увидеть потенциальный бонус для каждого сотрудника.
SELECT
	firstname,
	lastname,
	salary,
	department,
	CalculateAnnualBonus(employeeid, salary) AS Bonus
FROM
	employees
	
-- Задание 3: Представление (View): Создать представление с именем IT_Department_View, которое показывает 
-- EmployeeID, FirstName, LastName и Salary только для сотрудников из отдела 'IT'.
CREATE VIEW IT_Department_View AS
SELECT
	EmployeeID,
	FirstName,
	LastName,
	Salary
FROM
	employees
WHERE
	department = 'IT';

-- Задание 4: Выбрать данные из вашего представления IT_Department_View.
SELECT * FROM IT_Department_View