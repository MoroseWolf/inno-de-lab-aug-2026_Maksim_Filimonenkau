# Задача 1: Нормализация и сборка записи пользователя

raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"] 

def parse_task_1(user_record): 
    raw_parts = user_record.split(";")
    for i in range(4):
        part = raw_parts[i].strip()
        if i == 0:
            part = f"UUID-{part}"
        elif i == 1:
            part =  part.replace("_", " ").title() 
        elif i == 2:
            part =  part.upper()  
        elif i == 3:
            part =  part.lower() 
        raw_parts[i] = part 

    return " | ".join(raw_parts)


task_1 = parse_task_1(raw_user_record)
print(task_1)

task_2 = [
    int(pair.split(":")[1])
    for pair in raw_transactions
    if pair.split(":")[0] == "SUCCESS" and int(pair.split(":")[1]) > 0
    ]
print(task_2)