Python Dictionary to find mirror characters in a string

char = 'paradox'
k = 3

original = 'abcdefghijklmnopqrstuvwxyz'
reverse = 'zyxwvutsrqponmlkjihgfedcba'
dictChars = dict(zip(original,reverse))

prefix = char[0:k-1] 
suffix = char[k-1:] 
mirror = ''
  
for i in range(0,len(suffix)): 
    mirror = mirror + dictChars[suffix[i]] 
  
    # concat prefix and mirrored part 
print (prefix+mirror)

O/P::

paizwlc
