salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

period = range(0, months, 1)
for i in period:
    cost = salary - spend * (1 + increase) ** i
    need_money = need_money - cost


print(round(need_money))
