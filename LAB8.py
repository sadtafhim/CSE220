class Tree:
    def __init__(self,list):
        self.tree = list
        self.root = 0
    def height(self,p=0):
        if self.tree[self.root]==None:
            return 0
        else:
            m = ((2*p)+(2**p))-((2*p)+1)
            n = []
            for i in range(m):
                n.append(None)
            if 2**p == len(self.tree) or 2**p>len(self.tree):
                return -1
            if self.tree[((2*p)+1)-((2*p)+(2**p))]==n:
                return -1
            else:
                return self.height(p+1) + 1
    def level(self,n):
        m=self.tree
        def finder(x=0,list=m):
            if list[x]==n:
                return x
            else:
                return finder(x+1)
        u = finder()
        print(u)
        def level_maker(u,m=0):
            if u==0 or u<0:
                return m
            else:
                if u // 2 == 0:
                    m += 1
                    u = (u / 2) - 1
                    return level_maker(u, m)
                else:
                    m += 1
                    u = u // 2
            return level_maker(u, m)

        m = level_maker(u)
        return m
def similarity_checker(m1,m2):
    if m1.tree == m2.tree:
        print("yes")
    else:
        print("No")
def copy(m1):
    n = []
    for i in range(len(m1.tree)):
        n.append(m1.tree[i])
    x = Tree(n)
    print(x.tree)
    print(x)



l1 = Tree([1,2,3,4,5,6,7,8,9,10,11])
l2 = Tree([1,2,3,4,5,6,7,8,9,10,11])
print(l1.height())
print(l1.level(6))
similarity_checker(l1,l2)
copy(l1)
print(l1)

