import random


def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    #pass
    second_element = None
    try:
        second_element = L[1]
    except:
        pass
    return second_element

def create_list(min_size, max_size , min_value, max_value): 
    lista = []
    top_size = random.randint(min_size, max_size)
    for _ in range(top_size):
        lista.append(random.randint(min_value, max_value))
    return lista

def run():
    for i in range(99999999):
        lista = create_list(min_size = 0, max_size = 5, min_value = 1, max_value = 99)
        second_element = select_second(lista)
        print("Test "+ str(i) + " : " + str(lista) + "\t \t \t | 2nd element:" + str(second_element))
    
if __name__ == '__main__':
    run()
