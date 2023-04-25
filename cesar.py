
al_low_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
al_high_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
al_low_en = 'abcdefghijklmnopqrstuvwxyz'
al_high_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

########################################

def cesar_code_right(arg_1, arg_2):
    result = ''
    for item in arg_1:
        if item in al_high_ru:
            new_index = al_high_ru[al_high_ru.index(item) + int(arg_2) - len(al_high_ru)]
            result += new_index
        elif item in al_high_en:
            new_index = al_high_en[al_high_en.index(item) + int(arg_2) - len(al_high_en)]
            result += new_index
        elif item in al_low_ru:
            new_index = al_low_ru[al_low_ru.index(item) + int(arg_2) - len(al_low_ru)]
            result += new_index
        elif item in al_low_en:
            new_index = al_low_en[al_low_en.index(item) + int(arg_2) - len(al_low_en)]
            result += new_index
        else:
            result += item
    return print(result)


def cesar_code_left(arg_1, arg_2):
    result = ''
    for item in arg_1:
        if item in al_high_ru:
            new_index = al_high_ru[al_high_ru.index(item) - int(arg_2) - len(al_high_ru) + len(al_high_ru)]
            result += new_index
        elif item in al_high_en:
            new_index = al_high_en[al_high_en.index(item) - int(arg_2) - len(al_high_en) + len(al_high_en)]
            result += new_index
        elif item in al_low_ru:
            new_index = al_low_ru[al_low_ru.index(item) - int(arg_2) - len(al_low_ru) + len(al_low_ru)]
            result += new_index
        elif item in al_low_en:
            new_index = al_low_en[al_low_en.index(item) - int(arg_2) - len(al_low_en) + len(al_low_en)]
            result += new_index
        else:
            result += item
    return print(result)

########################################

def mode():
    text = str(input('Введите текст: '))
    text = text.replace('Ё', 'Е')
    text = text.replace('ё', 'е')
    while len(text) == 0:
        print('Поле обязательно!')
        text = str(input('Введите текст: '))
        text = text.replace('Ё', 'Е')
        text = text.replace('ё', 'е')

    k = input('Введите ключ:  ')
    while len(k) == 0 or not k.isdigit():
        print('Не гневи Цезаря!')
        k = input('Введите ключ:  ')

    lr = input('Шифруем или дешифруем?: "Ш/Д"  ')
    while len(lr) == 0 or not lr.lower() == 'ш' and not lr.lower() == 'д':
        print('Цезарь тебя не понимает!')
        lr = input('Шифруем или дешифруем?: "Ш/Д"  ')
    if lr.lower() == 'ш':
        return cesar_code_right(text, k)
    else:
        return cesar_code_left(text, k)

########################################

def repid():
    again = str(input('Продолжаем? "ДА/НЕТ"  '))
    while len(again) == 0 or not again.lower() == 'да':
        if again.lower() == 'нет':
            print('Авэ, Цезарь!')
            break
        else:
            print('Цезарь тебя не понимает!')
        again = str(input('Продолжаем? "ДА/НЕТ"  '))
    if again.lower() == 'да':
        return mode()


mode()
repid()

















