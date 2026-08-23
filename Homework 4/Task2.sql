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
update
	Employees
set
	email = case
		employeeid
        when 1 then 'alice.sm@mail.com'
		when 2 then 'bob.joh@mail.com'
		when 3 then 'charlie.br@mail.com'
		when 4 then 'diana.pr@mail.com'
		when 6 then 'dima.fil@mail.ru'
		when 7 then 'kris.Yli@mail.ru'
	end
where
	employeeid in (1, 2, 3, 4, 6, 7)
    
-- Задание 4: Добавить ограничение UNIQUE к столбцу Email в таблице
ALTER TABLE Employees 
ADD CONSTRAINT UQ_Email UNIQUE (Email)

-- Задание 5: Переименовать столбец Location
