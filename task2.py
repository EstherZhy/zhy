DEFAULT_COUNT = 0


def get_proportion_char(count_char):
    proportion_char = {}
    total = sum(count_char.values())
    for key in count_char.keys():
        proportion_char[key] = round(count_char[key] / total * 100, 1)
    return proportion_char


def get_count_char(str_):
    count_char = {}
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha():
            count_char[symbol] = count_char.get(symbol, DEFAULT_COUNT) + 1
    return count_char


main_str = """
       Данное предложение будет разбиваться на отдельные слова. 
       В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
       Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
   """
count_char = get_count_char(main_str)
print(count_char, sep='\n')