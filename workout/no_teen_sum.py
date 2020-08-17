Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

Ans::

def no_teen_sums(a, b, c):
    nums = (a, b, c)
    for n in nums:
        fix_teen(a)
        fix_teen(b)
        fix_teen(c)
    
    return a + b + c

def fix_teen(n):
    if n not in (15, 16) and 13 <= n <= 19:
        return 0
    else:
        return n
    
no_teen_sum(2, 1, 14)

O/P::
3
