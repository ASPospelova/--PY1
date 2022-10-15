src = not False and True or False and not True # исходное выражение

# result = True and True or False and False  # избавляемся от отрицаний
# result = True or False  # мзбавляемся от логического "И"
# result = True  # избавляемся от логического "ИЛИ"

result = True
print(src == result)
