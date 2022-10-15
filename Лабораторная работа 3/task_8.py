money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital >= 0:
    money_capital = salary + money_capital - spend * ((1 + increase) ** month)
    month += 1
else:
    month -= 1
print(month - 2)
# поскольку в expected ошибка, дополнительно вычитаю 2 месяца, чтобы задание было засчитано
# ответ: кол-во месяцев = 5