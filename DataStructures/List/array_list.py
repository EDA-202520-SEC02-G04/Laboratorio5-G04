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
    temp = my_list["elements"][pos1] 
    my_list["elements"][pos1] = my_list["elements"][pos2] 
    my_list["elements"][pos2] = temp 
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

def selection_sort(my_list, default_sort_criteria):
    for i in range(my_list["size"]):
        for j in range(i, my_list["size"]):
            if default_sort_criteria(my_list["elements"][j], my_list["elements"][i]):
                my_list = exchange(my_list, i, j)
    return my_list

def insertion_sort(my_list, default_sort_criteria):
    for i in range(my_list["size"]):
        j = i - 1
        while j >= 0 and  default_sort_criteria(my_list["elements"][i], my_list["elements"][j]):
            my_list = exchange(my_list, j, j + 1)
    return my_list

def shell_sort(my_list, default_sort_criteria):
    n = size(my_list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = get_element(my_list, i)
            j = i
            while j >= gap and not default_sort_criteria(get_element(my_list, j - gap), temp):
                change_info(my_list, j, get_element(my_list, j - gap))
                j -= gap
            change_info(my_list, j, temp)
        gap //= 2

    return my_list

def particion_quick_sort(my_list, sort_critera, lo, hi):
    pivote=first_element(my_list)
    i=lo+1
    for j in range(lo, hi):
        if get_element(my_list, j)< pivote:
            i+=1
            exchange(my_list, j, i)
    exchange(my_list, i+1, hi)
    return i+1
    
def quick_sort(my_list, default_sort_criteria, lo, hi):
    if lo< hi:
        x=particion_quick_sort(my_list, default_sort_criteria, lo, hi)
        quick_sort(my_list, default_sort_criteria, 0, x-1)
        quick_sort(my_list, default_sort_criteria, x+1, size(my_list))
    return my_list

def merge(my_list, left, right):
    mid = (left + right) // 2
    
    n1 = mid - left + 1
    n2 = right - mid
    L = new_list()
    R = new_list
    
    for i in range(n1):
        L = add_last(L, my_list["elements"][left + i])
    for j in range(n2):
        R = add_last(R, my_list["elements"][mid + 1 + j])
        
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            my_list["elements"][k] = L["elements"][i]
            i += 1
        else:
            my_list["elements"][k] = L["elements"][j]
            j += 1
        k += 1


    while i < n1:
        my_list["elements"][k] = L["elements"][i]
        i += 1
        k += 1

    while j < n2:
        my_list["elements"][k] = L["elements"][j]
        j += 1
        k += 1

def merge_sort(my_list, left, right):
    if left < right:
        
        mid = (right - left)//2
        merge_sort(my_list, left, mid)
        merge_sort(my_list, mid + 1, right)
        merge(my_list, left, right)
