def create_an_empty_list():
    empty_list = []
    return empty_list

def create_a_list():
    four_elements = [1,2,3,4]
    return four_elements

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l
    return None

def remove_element_from_start_of_list(l):
    del(l[0])
    return l
    return None

def retrieve_first_element_from_list(l):
    return l[0]
    return None

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
    return None
