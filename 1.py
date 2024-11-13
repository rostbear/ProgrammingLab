my_list = [2, 1, 14]

def sum_list(my_list):
    if(len(my_list) == 0):
        return None

    somma = 0;
    for i in range(len(my_list)):
        somma = somma + my_list[i]
    return somma

print("La somma di my_list è: {}".format(sum_list(my_list)))