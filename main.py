import os
import time
def init_cook_book():
    cook_book = {}
    with open('recipes.txt', encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            num = int(file.readline())
            h = list()
            for i in range(num):
                ingredients = {}
                ingredient = file.readline().strip()
                ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingredient.split('|')
                ingredients['quantity'] = int(ingredients['quantity'])
                h.append(ingredients)
            file.readline()
            cook_book[name] = h
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    names_dishes_list = []
    final_cook = {}
    for dish in dishes:
        name_dish = dish
        for key, value in cook_book.items():
            if name_dish in key:
                names_dishes_list.append(value)
                for name_dish_list in names_dishes_list:
                    for ty in name_dish_list:
                        name_igredient = ty['ingredient_name']
                        name_measure = ty['measure']
                        quantity = ty['quantity'] * person_count
                        gh = {'measure': name_measure, 'quantity' : quantity}
                        final_cook.update({name_igredient: gh})
    return final_cook
def read_file():
    file_1 = '/home/vladpyrkov/Files/files/1.txt'
    file_2 = '/home/vladpyrkov/Files/files/2.txt'
    file_3 = '/home/vladpyrkov/Files/files/3.txt'
    if file_1 or file_2 or file_3 is None:
        text_1 = '/home/vladpyrkov/Files/files/1.txt'
        text_2 = '/home/vladpyrkov/Files/files/2.txt'
        text_3 = '/home/vladpyrkov/Files/files/3.txt'
        name_text_1 = os.path.basename(r'/home/vladpyrkov/Files/files/1.txt')
        name_text_2 = os.path.basename(r'/home/vladpyrkov/Files/files/2.txt')
        name_text_3 = os.path.basename(r'/home/vladpyrkov/Files/files/3.txt')
        outout_text = '/home/vladpyrkov/Files/files/file_finish.txt'
        with open(text_1,'r', encoding="utf-8") as file_1:
            file_1_readline = file_1.readlines()
        with open(text_2,'r', encoding="utf-8") as file_2:
            file_2_readline = file_2.readlines()
        with open(text_3,'r', encoding="utf-8") as file_3:
            file_3_readline = file_3.readlines()
        with open(outout_text,'w', encoding="utf-8") as outout_file:
            len_file_1 = len(file_1_readline)
            len_file_2 = len(file_2_readline)
            len_file_3 = len(file_3_readline)
            text = {len_file_1:[{name_text_1: file_1_readline}], len_file_2:[{name_text_2: file_2_readline}], len_file_3:[{name_text_3: file_3_readline}]}
            list_keys = list(text.keys())
            list_keys.sort()
            for i in list_keys:
                line_num = str(i)
                for g in text[i]:
                    line_name = g.keys()
                    for name in line_name:
                        name_text = name
                        line_text = g.values()
                        for lines in line_text:
                            li = ''.join(lines)             
                            outout_file.write(name_text + '\n')
                            outout_file.write(line_num + '\n')
                            outout_file.write(li + '\n')
if __name__ == '__main__':
    print('----------------Задание 1----------------')
    cook_book = init_cook_book()
    print(cook_book)
    time.sleep(1)
    print('----------------Задание 2----------------')
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    time.sleep(1)
    print('----------------Задание 3----------------')
    read_file()