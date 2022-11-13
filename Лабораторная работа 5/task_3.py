from random import randint

first = -10
second = 10
len_list = 15

def get_unique_list_numbers() -> list[int]:
   list_of_unique_num = []
   while len(list_of_unique_num) != len_list:
      num = randint(first, second)
      if num not in list_of_unique_num:
         list_of_unique_num.append(num)
   return list_of_unique_num


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
