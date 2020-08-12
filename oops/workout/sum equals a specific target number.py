Write a Python class to find a pair of index of elements from a given array whose sum equals a specific target number. - Go to the editor
Input: numbers= [10,20,10,40,50,60,70], target=50

Ans::

class py_solution:
    def twoSum(self,numbers,target):
        n = []

        for x in numbers:
            if x < target:
                n.append(x)
        else:
            pass

        m = list(set(n))

        for i in range (len(m)):
            for j in range (1,len(m)):
                if (m[i]+m[j]) == target:
                    print(numbers.index(m[j]),numbers.index(m[i]))
                    
if __name__=="__main__":
    numbers= [5,20,10,40,50,60,70]
    target=50
    obj = py_solution()
    obj.twoSum(numbers,target)
    
O/P::
2 3
