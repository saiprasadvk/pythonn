Python | Sort a tuple by its float element


Input : tuple = [('lucky', '18.265'), ('nikhil', '14.107'), 
                  ('akash', '24.541'), ('anand', '4.256'), ('gaurav', '10.365')]
Output : [('akash', '24.541'), ('lucky', '18.265'), 
          ('nikhil', '14.107'), ('gaurav', '10.365'), ('anand', '4.256')]

Ans::
def Sort(tup): 
    tup.sort(key = lambda x: float(x[1]), reverse = True) 
    print(tup)
    
    
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),('anand', '4.256'), ('gaurav', '10.365')] 
Sort(tup)

O/P::
[('akash', '24.541'), ('lucky', '18.265'), ('nikhil', '14.107'), ('gaurav', '10.365'), ('anand', '4.256')]
