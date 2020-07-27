#Print unique rows in a given boolean matrix using Set with tuples

Ans:

mat = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 1, 1, 0, 0]]

inputs = set(map(tuple, mat))

for i in list(inputs):
    print(i)
    
O/P::

(1, 1, 1, 0, 0)
(0, 1, 0, 0, 1)
(1, 0, 1, 1, 0)

    
    
