# Задача 1: Нормализация и сборка записи пользователя
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# Задача 2: Фильтрация транзакций платежного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50",
                    "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

# Задача 3: Безопасный парсинг конфигурации API
db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

# Задача 4: Аудит прав доступа и дедупликация
# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin",
                   "developer", "guest"]
# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer",
                        "audit_manager"}


def parse_task_1(user_record):
    raw_parts = user_record.split(";")
    for i in range(4):
        part = raw_parts[i].strip()
        if i == 0:
            part = f"UUID-{part}"
        elif i == 1:
            part = part.replace("_", " ").title()
        elif i == 2:
            part = part.upper()
        elif i == 3:
            part = part.lower()
        raw_parts[i] = part

    return " | ".join(raw_parts)


def parse_dict_task_3(config):
    connection = config["connection"]
    host = connection["host"]
    port = connection["port"]
    ssl_settings = connection.get(
        "ssl_settings", {}).get("ssl_mode", "verify-full")

    connection["user"] = "admin"
    connection["max_connections"] = 100
    connection["ssl_mode"] = ssl_settings
    return config


def audit_task_4(roles, admin_roles):
    roles_set = set(roles)
    common_roles = roles_set.intersection(admin_roles)
    difference_roles = admin_roles.difference(roles_set)
    find_flag = False
    if "security_officer" in roles_set:
        find_flag = True

    return roles_set, common_roles, difference_roles,  find_flag


print("Задание 1:")
task_1 = parse_task_1(raw_user_record)
print(f"Нормализованная запись: {task_1}\n")

print("Задание 2:")
task_2 = [
    int(pair.split(":")[1])
    for pair in raw_transactions
    if pair.split(":")[0] == "SUCCESS" and int(pair.split(":")[1]) > 0
]
print(f"Очищенные транзакции: {task_2}\n")

print("Задание 3:")
task_3 = parse_dict_task_3(db_config)
print(
    f"SSL Mode: {task_3["connection"]["ssl_mode"]}\nПараметры соединения:")
for key, value in task_3["connection"].items():
    if key == "ssl_mode":
        continue
    print(f"* {key}: {value}")

print("\nЗадание 4:")
unique_set, common_set, difference_set, flag = audit_task_4(
    requested_roles, required_admin_roles)
print(f"""Уникальные запрошенные роли: {unique_set} 
Общие административные роли: {common_set} 
Недостающие административные роли: {difference_set} 
Наличие роли security_officer в запросе: {flag}\n""")
