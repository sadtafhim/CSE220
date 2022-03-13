#1

def selection_sort(list,min_index=0):
    def selection_sorter(list,d=1,q=0,x=0):
        def selection_sorter2(list,m,n):
            if n==len(list):
                if list[x]>list[m]:
                    y = list[m]
                    list[m] = list[x]
                    list[x] = y
                else:
                    pass
            else:

                if list[m]>list[n]:
                    m=n
                return selection_sorter2(list,m,n+1)

        if d == len(list):
            return
        else:

            selection_sorter2(list, q+1, d+1)
            return selection_sorter(list, d+1,q+1,x+1)
    if min_index == len(list):
        return list
    else:
        selection_sorter(list)
        return selection_sort(list,min_index+1)
print(selection_sort([4,2,6,5,1,3]))
#2
def insertionSortRecursive(list,x):
    if x <= 1:
        return
    insertionSortRecursive(list, x - 1)
    u = list[x - 1]
    m = x - 2

    while (m >= 0 and list[m] > u):
        list[m + 1] = list[m]
        m = m - 1

    list[m + 1] = u

    return list
list = [4,2,1,5,3]
print(insertionSortRecursive(list , len(list)))

#3
class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n

class LinkedList:

    def __init__(self, a, nxt = None):
        if len(a)==0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            for i in range(len(a)):
                if i == 0:
                    new_node = Node(a[i], nxt)
                    self.head = new_node
                    self.tail = new_node
                    self.length = 1
                else:
                    new_node = Node(a[i],nxt)
                    self.tail.next = new_node
                    self.tail = new_node
                    self.length += 1

    def shorter(self,a=0):
        while a!=self.length:
            self.now = self.head
            self.n = self.head.next
            for i in range(self.length):
                if self.n == None:
                    break
                else:
                    if self.now.elem>self.n.elem:
                        x = self.now.elem
                        self.now.elem = self.n.elem
                        self.n.elem = x
                        self.now = self.now.next
                        self.n = self.n.next
                    else:
                        self.now = self.now.next
                        self.n = self.n.next
            a+=1

    def showList(self):
        m = self.head
        if self.length == 0:
            print("Empty List!")
        else:
            count = 0
            while m != None:
                if count == self.length -1:
                    print(m.elem, )
                    m = m.next
                    count += 1
                else:
                    print(m.elem, end=" ")
                    m = m.next
                    count += 1
a = [20, 30, 10, 60, 50, 40]
l1 = LinkedList(a)
l1.shorter()
l1.showList()
#4
class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n

class LinkedList:

    def __init__(self, a, nxt = None):
        if len(a)==0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            for i in range(len(a)):
                if i == 0:
                    new_node = Node(a[i], nxt)
                    self.head = new_node
                    self.tail = new_node
                    self.length = 1
                else:
                    new_node = Node(a[i],nxt)
                    self.tail.next = new_node
                    self.tail = new_node
                    self.length += 1

    def shorter(self):
        self.start = self.head
        self.point = self.head
        min = self.start
        for i in range(self.length):
            while self.point != None:
                if self.point.elem<self.start.elem:
                    min = self.point
                    self.point = self.point.next
                else:
                    self.point = self.point.next
            if min ==self.start:
                self.start = self.start.next
                self.point = self.start
                min = self.start
            else:
                x = self.start.elem
                self.start.elem = min.elem
                min.elem = x
                self.start = self.start.next
                self.point = self.start
                min = self.start



    def showList(self):
        m = self.head
        if self.length == 0:
            print("Empty List!")
        else:
            count = 0
            while m != None:
                if count == self.length -1:
                    print(m.elem, )
                    m = m.next
                    count += 1
                else:
                    print(m.elem, end=" ")
                    m = m.next
                    count += 1
a = [20, 30, 10, 60, 50, 40]
l1 = LinkedList(a)
l1.shorter()
l1.showList()
#5
class Node:
    def __init__(self, e, n,p):
        self.elem = e
        self.next = n
        self.prev = p

class LinkedList:

    def __init__(self, a, nxt = None,prev=None):
        if len(a)==0:
            self.head = None
            self.tail = None
            self.prev = None
            self.length = 0
        else:
            for i in range(len(a)):
                if i == 0:
                    new_node = Node(a[i], nxt,prev)
                    self.head = new_node
                    self.tail = new_node
                    self.length = 1

                else:
                    new_node = Node(a[i], nxt, prev)
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                    self.length += 1
    def sorter(self):
        for i in range(self.length-1):
            self.x = self.head
            self.y = self.head.next
            for j in range(self.length-1):
                if self.x ==None:
                    break
                else:
                    if self.x.elem>self.y.elem:
                        y = self.x.elem

                        self.x.elem = self.y.elem
                        self.y.elem = y
                        self.x = self.x.prev
                    else:
                        self.x.prev
                    self.x = self.y
                    self.y = self.y.next


    def showList(self):
        m = self.head
        if self.length == 0:
            print("Empty List!")
        else:
            count = 0
            while m != None:
                if count == self.length - 1:
                    print(m.elem, )
                    m = m.next
                    count += 1
                else:
                    print(m.elem, end=" ")
                    m = m.next
                    count += 1
    def reverseshowList(self):
        m = self.tail
        if self.length == 0:
            print("Empty List!")
        else:
            count = 0
            while m != None:
                if count == self.length - 1:
                    print(m.elem, )
                    m = m.prev
                    count += 1
                else:
                    print(m.elem, end=" ")
                    m = m.prev
                    count += 1

a = [20, 30, 10, 60, 50, 40]
l1 = LinkedList(a)
l1.showList()
l1.sorter()
l1.showList()
#6
def binary_search(my_list, low, high, elem):
    if high >= low:
        mid = (high + low) // 2
        if my_list[mid] == elem:
            return mid
        elif my_list[mid] > elem:
            return binary_search(my_list, low, mid - 1, elem)
        else:
            return binary_search(my_list, mid + 1, high, elem)
    else:
        return -1


my_list = [1, 9, 11, 21, 34, 54, 67, 90]
elem_to_search = 1
my_result = binary_search(my_list, 0, len(my_list) - 1, elem_to_search)
if my_result != -1:
   print("Index", str(my_result))
else:
   print("Not found!")
#7
fibonacci_store = [1,1]
def fibonacci(x):
    if x<=len(fibonacci_store):
        return fibonacci_store[x-1]

    else:
        fibo = fibonacci(x-1)+fibonacci(x-2)
        fibonacci_store.append(fibo)
        return fibo

print(fibonacci(5))

