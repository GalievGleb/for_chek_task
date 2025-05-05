monday = int(input(f"Привет! сколько кейсов в понедельник?"))
vtornik = int(input(f"сколько кейсов в вторник?"))
sreda = int(input(f"сколько кейсов в среду?"))
chetverg = int(input(f"сколько кейсов в четверг?"))
friday = int(input(f"а в пятницу?"))
total = monday + vtornik + sreda + chetverg + friday
avg = total//5
print(f"Общее количество кейсов - {total} за неделю , в среднем в день {avg}")
if avg > 10:
    print("Отличная работа")
else: print(f"Попробуй улучшить результат")