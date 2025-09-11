def new_list():
    newlist = {'elements': [], 'size': 0,}
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list,element,cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range (0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element,info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def add_first(my_list, element):
    newlist = [element]
    for i in range(size(my_list)):
        newlist.append(my_list['elements'][i])
    my_list['size'] += 1
    my_list['elements'] = newlist
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] +=1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list['elements'][0]

def is_empty(my_list):
    if len(my_list['elements']) == 0:
        return True
    return False

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list['elements'][-1]

def delete_element(my_list, pos):
    my_list['size'] -= 1
    my_list['elements'].pop(pos)
    return my_list
    
def remove_first(my_list):
    if my_list["size"] == 0:
        return None
    my_list["size"] -= 1
    return my_list["elements"].pop(0)

def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    my_list["size"] -= 1
    return my_list["elements"].pop(-1)

def insert_element(my_list, element, pos):
    index = 0
    nueve_lista = new_list()
    while index < my_list["size"]:
        add_last(nueve_lista,my_list["elements"][index])
        if index == pos:
            add_last(nueve_lista,element)
        index += 1                  
    return nueve_lista
    

def change_info(my_list, pos, element):
    my_list['elements'][pos] = element
    return my_list

def exchange(my_list, pos1, pos2):
    newlist = my_list
    change_info(newlist, pos1, my_list['elements'][pos2])
    change_info(newlist, pos2, my_list['elements'][pos1])
    my_list['elements'] = newlist
    return my_list

def sub_list(my_list, pos_i, num_elements):
    my_list['size'] -= pos_i
    my_list['elements'] = my_list['elements'][pos_i:num_elements + pos_i]
    return my_list

def default_sort_criteria(element_1,element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list):
    for i in range(my_list["size"]):
        for j in range(i, my_list["size"]):
            if my_list["elements"][j] < my_list["elements"][i]:
                temp = j
        my_list = exchange(my_list, i, temp)
    return my_list