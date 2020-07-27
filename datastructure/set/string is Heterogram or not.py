Check whether a given string is Heterogram or not

Ans::

S = "the big dwarf only jumps"

def Heterogram(S):
    tmpSet = []
    for ch in S:
        if (ord(ch)>=ord('a') and ord(ch)<=ord('z')):
            print(ch)
            tmpSet.append(ch)
    if len(set(tmpSet)) == len(tmpSet):
        print("yes")
    else:
        print("No")
        
 O/p:
 yes
