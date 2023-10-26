import itertools 
input_string = str(input("enter your string : "))
n = len(input_string)
input_string = input_string.split(' ')


combinations = []
for i in range(0,n) :

    combinations = itertools.combinations(input_string,i)
    new_list = list(combinations)
    #we created one bog new list of combinations produced by the itertools.combinations() fn.
    new_list.extend(combinations)
    print(new_list)

