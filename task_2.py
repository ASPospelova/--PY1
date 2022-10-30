dictionary = {}
numbers = 0
def get_count_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for thing in str_:
        if thing.isalpha() is True and thing not in dictionary:
            dictionary[thing] = 1
        elif thing.isalpha() is True and thing in dictionary:
            dictionary[thing] += 1
    return dictionary

def new_dictionary(dictionary):
    number = sum(dictionary.values())
    for sumbol in dictionary:
        dictionary = round(dictionary[sumbol] / number * 100, 1)
    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
