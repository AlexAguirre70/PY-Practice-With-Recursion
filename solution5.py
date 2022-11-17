# Write code for algorithm 5 below
def palin(my_string):
    if len(my_string)==1:
        return True
    else:
        if my_string[0]==my_string[-1]:
            return palin(my_string[1:-1])
        else:
            return False

print(palin("repaper"))
