def tuple_without(original_tuple, element_position_to_remove): #remove elements i from tuple
    new_tuple = ()
    i=0
    for s in list(original_tuple):
        if i != element_position_to_remove:
            new_tuple = new_tuple +(s,)
        i=i+1
    return new_tuple

def equal_tuples(tuple_a,tuple_b):
    if(not isinstance(tuple_a,tuple)): return False
    if(not isinstance(tuple_b,tuple)): return False
    if (len(tuple_a) != len(tuple_b)): return False
    for i in range(0,len(tuple_a)-1):
        if (tuple_a[i] != tuple_b[i]): return False
    return True