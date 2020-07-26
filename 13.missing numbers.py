1. Find the missing numbers in between
i/o : [1,2,10,12]
o/p : [3,4,5,6,7,8,9,11]

Ans::
sol1:
I = [1,2,10,12]

I1 = []

for x in range(1,12):
    if x not in I:
        I1.append(x)

print(I1)

sol2:

def missing_numbers(num_list):
    orginal_list = [x for x in range((num_list[0]), num_list[-1]+1)]
    num_list = set(num_list)
    return list(num_list ^ set(orginal_list))
I = [1,2,10,12]

print(missing_numbers(I))

O/p:
[3,4,5,6,7,8,9,11]

