9. IF dictionary has duplicate value then group the keys and formed new dictionary i/o = {'a':1,'b':1,'c':1,'d'2} o/p - {('a','b','c'):1,'d':2}


Ans:

ip = {'a':1,'b':1,'c':1,'d':2}
set_ip = set(ip.values())

d = {}
for n in set_ip:
    d[n] = [k for k in ip.keys() if ip[k] == n]
print(d)

d = {tuple(value):key for key, value in d.items()}

O/P:

{1: ['a', 'b', 'c'], 2: ['d']}
