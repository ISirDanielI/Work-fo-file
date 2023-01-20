import os

this_location = os.getcwd()
folder_name = 'data'
file_name = 'recept.txt'
full_path = os.path.join(this_location, folder_name, file_name)

cook_book = {}
with open(full_path, 'r') as f:
    eat = {}
    for line in f:
        eat_name = line.strip()
        quantity_eat = int(f.readline())
        products = []
        for _ in range(quantity_eat):
            prod = f.readline().strip().split(' | ')
            ingridient, quantity, measure = prod
            products.append({'ingredient_name': ingridient, 'quantity': quantity, 'measure': measure})
        cook_book[eat_name] = products
        f.readline()

dishes = ["Омлет", "Запеченный картофель"]
person_count = 3


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            new_shop_list = dict(ingr)
            new_shop_list["quantity"] = int(new_shop_list["quantity"]) * person_count
            if new_shop_list["ingredient_name"] not in shop_list:
                shop_list[new_shop_list["ingredient_name"]] = new_shop_list
            else:
                shop_list[new_shop_list["ingredient_name"]]["quantity"] += new_shop_list["quantity"]
    return shop_list

print(get_shop_list_by_dishes(dishes, person_count))

file_name_two = '1.txt', '2.txt'

def col():
    operation = 0
    ent_puth = os.path.join(this_location, folder_name, '3.txt')
    file_ent = open(ent_puth, 'w')
    if file_one_sum > file_two_sum:
        operation += 1
        file_ent.write(file_two_name + '\n')
        file_ent.write(str(file_two_sum) + '\n')
        if operation == 1:
            with open(full_path_two, 'r') as f:
                for _ in range(file_two_sum):
                    file_ent.write(f.read() + '\n')
        file_ent.write(file_one_name + '\n')
        file_ent.write(str(file_one_sum) + '\n')
        operation += 1
        if operation == 2:
            with open(full_path_one, 'r') as f:
                file_ent.write(f.read() + '\n')
        file_ent.close()
        return ''



operation = 0
for fname in file_name_two:
    full_path_other = os.path.join(this_location, folder_name, fname)
    full_path_one = os.path.join(this_location, folder_name, '1.txt')
    full_path_two = os.path.join(this_location, folder_name, '2.txt')
    with open(full_path_other,'r') as f:
        if fname == '1.txt':
            file_one_name = fname
            file_one_sum = sum(1 for _ in f)
            operation += 1
        if fname == '2.txt':
            file_two_name = fname
            file_two_sum = sum(1 for _ in f)
            operation += 1
        if operation >= len(file_name_two):
            print(col())

