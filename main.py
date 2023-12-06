from pprint import pprint

def my_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li

    return cook_book
cook_book_2 = my_cook_book()
pprint(cook_book_2)

def get_shop_list_by_dishes(dishes, person_count):
    get_shop_dict = {}
    for dish in dishes:
        for ingredient in cook_book_2[dish]:
            if ingredient['ingredient_name'] in get_shop_dict:
                get_shop_dict[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                get_shop_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    pprint(get_shop_dict)


get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)

