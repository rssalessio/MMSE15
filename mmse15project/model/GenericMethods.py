def tuple_without(original_tuple, element_position_to_remove): #remove elements i from tuple
    new_tuple = ()
    i=0
    for s in list(original_tuple):
        if i != element_position_to_remove:
            new_tuple = new_tuple +(s,)
        i=i+1
    return new_tuple