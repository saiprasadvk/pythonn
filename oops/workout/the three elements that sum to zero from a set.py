Write a Python class to find the three elements that sum to zero from a set
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]

Ans::

class elements:
    def Sum(self,I):
        j = len(sorted(I))
        result = []
        for x in range(j):
            for y in range (1,j):
                for z in range (2,j):
                    if I[x]+I[y]+I[z] == 0:
                        result.append([I[x], I[y], I[z]])

        res = list(set(tuple(sorted(sub)) for sub in result))
        print(res)

if __name__=="__main__":
    I = [-25, -10, -7, -3, 2, 4, 8, 10]
    obj = elements()
    obj.Sum(I)
    
O/P::

[(-7, -3, 10), (-10, 2, 8)]
