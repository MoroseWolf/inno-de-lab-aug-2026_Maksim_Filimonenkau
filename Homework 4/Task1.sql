-- Задание 1: вставить 2 новые записи в таблицу Employees
INSERT
    INTO
    Employees (FirstName,
    LastName,
    Department,
    Salary)
VALUES 
('Dmitriy',
'Filkin',
'HR',
'28000.00'),
('Kris',
'Ylianka',
'Finance',
'210800.00');

-- Задание 2: Вывести список всех сотрудников из Employees
SELECT
    *
FROM
    Employees

-- Задание 3: Выбрать только FirstName и LastName сотрудников из отдела 'IT'. 
SELECT
    FirstName,
    LastName
FROM
    Employees
WHERE
    Department = 'IT'

-- Задание 4: Обновить Salary 'Alice Smith' до 65000.00. 
UPDATE
    employees
SET
    Salary = 65000.00
WHERE
    FirstName = 'Alice'
    AND Lastname = 'Smith'

-- Задание 5: Удалить сотрудника 'Eve Davis'.
DELETE
FROM
    employees
WHERE
    concat(FirstName, ' ', LastName) = 'Eve Davis'

-- Задание 6: Проверить все изменения, используя SELECT * FROM Employees.
SELECT
    *
FROM
    Employees
