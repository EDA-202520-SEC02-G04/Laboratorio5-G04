from DataStructures.List import list_node as ln

def new_list():
    newlist = {"first": None, "last":None, "size":0,}
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    nodo_nuevo = ln.new_single_node(element)
    nodo_nuevo["next"] = my_list["first"]
    my_list["first"] = nodo_nuevo
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
    my_list["size"] += 1
    return my_list
    
def add_last(my_list, element):
    nodo_nuevo = ln.new_single_node(element)
    nodo_nuevo["next"] = None  

    if my_list["size"] == 0:  
        my_list["first"] = nodo_nuevo
        my_list["last"] = nodo_nuevo
    else:
        my_list["last"]["next"] = nodo_nuevo  
        my_list["last"] = nodo_nuevo          
    
    my_list["size"] += 1
    return my_list
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list['first'] is not None:
        return my_list['first']['info']
    return None

def last_element(my_list):
    if my_list["last"] is not None:
        return my_list["last"]["info"]
    return None

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    anterior = None
    index = 0
    while index < pos:
        anterior = actual
        actual = actual["next"]
        index += 1
        
    eliminado = actual

    if anterior is None:
        
        my_list["first"] = actual["next"]
        if my_list["size"] == 1:   
            my_list["last"] = None
    else:
        
        anterior["next"] = actual["next"]
        if actual == my_list["last"]:  
            my_list["last"] = anterior

    my_list["size"] -= 1
    return eliminado  

            
def remove_first(my_list):
    eliminado = delete_element(my_list,0)
    if eliminado is None:
        return None
    else:
        return eliminado["info"]

def remove_last(my_list):
    eliminado = delete_element(my_list,my_list["size"]-1)
    if eliminado is None:
        return None
    else:
        return eliminado["info"]
    
def change_info(my_list,pos,new_info):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    index = 0
    while index < 0:
        actual = actual["next"]
        index += 1
    actual["info"] = new_info
    return actual
        
def exchange(my_list,pos_1,pos_2):
    if pos_1 and pos_2< 0 or pos_1 and pos_2 >= my_list["size"]:
        return None
    actual_pos_1 = my_list["first"]
    actual_pos_2 = my_list["first"]
    index_1 = 0
    index_2 = 0
    while index_1 < pos_1:
        actual_pos_1 = actual_pos_1["next"]
        index_1 += 1
    while index_2 < pos_2:
        actual_pos_2 = actual_pos_2["next"]
        index_2 += 1
    nuevo_pos_1 = actual_pos_1
    actual_pos_1["info"] = actual_pos_2["info"]
    actual_pos_2["info"] = nuevo_pos_1["info"]
    return actual_pos_2
    
    
def sub_list(my_list,pos,num_elements):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    index = 0
    nueva_lista = new_list()
    add_last(nueva_lista,actual["info"])
    while index < pos:
        actual = actual["next"]
        add_last(nueva_lista,actual["info"])
        index += 1
        nueva_lista["size"] = num_elements
    return nueva_lista
        

def insert_element(my_list,element,pos):
    if pos < 0 or pos >= my_list["size"]:
        return None
    actual = my_list["first"]
    index = 0
    nueva_lista = new_list()
    add_last(nueva_lista,actual["info"])
    while index < pos:
        actual= actual["next"]
        add_last(nueva_lista,actual["info"])
        if index == pos:
            actual["info"] = element
            add_last(nueva_lista,actual["info"])
        index += 1
        nueva_lista["size"] += 1
    return nueva_lista
    
        
    
    
        
    
        
    