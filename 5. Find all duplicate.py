5. Find all duplicate and their count from the list 
  - Should not used any inbuild functionalities (like counter) i/o - [1,1,1,2,2,3,4,5,6] o/p - 1 is 3 times 2 is 2 times
  
 Ans::
sol1:
  
 I = [1,1,1,2,2,3,4,5,6]
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for x in I:
    if x == 1:
        one += 1
    elif x == 2:
        two += 1
    elif x == 3:
        three += 1
    elif x == 4:
        four += 1
    elif x == 5:
        five += 1
    elif x == 6:
        six += 1
        
print("1 is",one, "times")
print("2 is",two, "times")

sol2:
  
listOfElems = [1,1,1,2,2,3,4,5,6]

def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1
            
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    return dictOfElems

dictOfElems = getDuplicatesWithCount(listOfElems)     
for key, value in dictOfElems.items():
        print(key , 'is', value, "times")

O/P:

1 is 3 times
2 is 2 times
