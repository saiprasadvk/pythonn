class MyList(object):
    data = None
    Next = None

    def __init__(self,val):
        self.val = val
        self.head = None

    @classmethod
    def add(cls,val):
        if not cls.data:
            head = cls(val)
            cls.data = head
            cls.Next = head
        else:
            head = cls(val)
            cls.Next.head = head
            cls.Next = head
        return cls.data

    def view(self):
        iter_list = MyList.data
        while iter_list:
            print(iter_list.val)
            iter_list = iter_list.head


if __name__=="__main__":
    x = [2,3,4,6,7]
    for i in x:
        obj = MyList.add(i)
    obj.view()    
    
O/P:
2
3
4
6
7
