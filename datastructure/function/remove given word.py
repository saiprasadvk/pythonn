Python3 program to remove Nth occurrence of the given word 


Ans::

def Remove(Str,word,n):
    newword = []
    count = 0
    for x in Str:
        if x == word:
            count += 1
            if (count != n):
                newword.append(x)
        else:
            newword.append(x)
    lst = newword
    
    if count == 0: 
        print("Item not found") 
    else: 
        print("Updated list is: ", lst)	 

    return newword 

# Driver code 
l = ["geeks", "for", "geeks"] 
word = "geeks"
N = 1

Remove(l, word, N)


O/P::

Updated list is:  ['for', 'geeks']
