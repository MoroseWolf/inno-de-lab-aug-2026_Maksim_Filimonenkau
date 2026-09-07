-- Задание 1: Создать таблицу Departments
CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
"Location" VARCHAR(50)
)

-- Задание 2: Изменить таблицу Employees
ALTER TABLE Employees
ADD Email VARCHAR(100);

-- Задание 3: Заполнить столбец Email для всех сотрудников
UPDATE
	Employees
SET
	email = CASE
		employeeid
        WHEN 1 THEN 'alice.sm@mail.com'
		WHEN 2 THEN 'bob.joh@mail.com'
		WHEN 3 THEN 'charlie.br@mail.com'
		WHEN 4 THEN 'diana.pr@mail.com'
		WHEN 6 THEN 'dima.fil@mail.ru'
		WHEN 7 THEN 'kris.Yli@mail.ru'
	END
WHERE
	employeeid IN (1, 2, 3, 4, 6, 7)

-- Задание 4: Добавить ограничение UNIQUE к столбцу Email в таблице
ALTER TABLE Employees 
ADD CONSTRAINT UQ_Email UNIQUE (Email)
	
-- Задание 5: Переименовать столбец Location
ALTER TABLE Departments RENAME COLUMN "Location" TO OfficeLocation