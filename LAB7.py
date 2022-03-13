#1
class KeyIndex:
    def __init__(self,list):
        self.list = list
        self.min = 0
        new_list = []
        max = 0
        for i in self.list:
            if i > max:
                max = i
            elif i < self.min:
                self.min = i
        if self.min<0:
            self.min = self.min*-1
            for i in range(len(self.list)):
                self.list[i]=self.list[i]+self.min
            self.min = self.min*-1
            for i in self.list:
                if i>max:
                    max = i
        for i in range(max+1):
            new_list.append(0)
        for n in self.list:
            new_list[n]+=1
        self.list = new_list
    def print_key(self):
        print(self.list)
    def search(self,int):
        self.int = int
        min = self.min*-1
        self.int +=min
        if self.list[self.int] !=0:
            return True
        else:
            return False
    def sort(self):
        list = []
        for i in range(len(self.list)):
            if self.list[i] !=0:
                for j in range(self.list[i]):
                    list.append(i+self.min)
        return list

a = [4,-2,-3,4,7,4]
l1 = KeyIndex(a)
l1.print_key()
print(l1.search(5))
print(l1.sort())

#2
def hash(list):
    consonant = ['BCDFGHJKLMNPQRSTVWXYZ']
    numbers = '1234567890'
    hash_table = []
    for i in range(9):
        hash_table.append(None)
    for j in list:
        num = 0
        cons = 0
        for n in j:
            if n in numbers:
                num+= int(n)
            elif n in consonant:
                cons+=1
            else:
                continue
        value =(cons*24+num)%9
        if hash_table[value]==None:
            hash_table[value]=j
        else:
            for i in range(len(hash_table)):
                if hash_table[i]==None:
                    hash_table[i]=j
                    break
                else:
                    continue
    print(hash_table)

x = ['ST1E89B8A32','ST1E89B8A32','ST1E89B8A32']
hash(x)