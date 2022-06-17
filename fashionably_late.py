def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    #arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford', 'Calabaza', 'Coqueta']
    #found_in_list = False
    fashionably_late = False
    #print(arrivals)
    list_size = len(arrivals)
    #print(list_size)
    #name = 'Ford'
    counter = 0
    for element in arrivals:
        counter +=1 
        if name == element:
            if counter < list_size and counter > round(list_size/2):
                fashionably_late = True
                break
            else:
                pass
    return fashionably_late

# Check your answer
#q5.check()