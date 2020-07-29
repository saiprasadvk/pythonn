Write a Python function that takes a list and returns a new list with unique elements of the first list


Ans::

def Unique(L):
    ul = []
    for i in L:
        if i not in ul:
            ul.append(i)
        else:
            pass
            
    return ul        

sample_list = [1,2,3,3,3,3,4,5]
Unique(sample_list)

O/P:

[1, 2, 3, 4, 5]
