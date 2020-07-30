Ans:

Open = ['{','[','(']
Close = ['}',']',')']

def symbolcheck(Str):
    o = []
    for i in Str:
        if i in Open:
            print('open',i)
            o.append(i)
        elif i in Close:
            print('close',i)
            c = Close.index(i)
            print(c)
            if ((len(o) > 0 and (Open[c] == o[len(o) -1]))):
                print(o)
                o.pop()
            else:
                return "Unbalanced"
    
    if len(o) == 0:
        return "balanced"
    else:
        return "Unbalanced"           
        
  
Srt = "()()"
symbolcheck(Srt)

O/p:

Balanced
