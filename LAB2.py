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


    def showList(self):
        m = self.head
        if self.length == 0:
            print("Empty List!")
        else:
            count = 0
            while m != None:
                if count == self.length-1:
                    print(m.elem ,)
                    m = m.next
                    count += 1
                else:
                    print(m.elem,end=" ")
                    m = m.next
                    count += 1
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, newElement, index = None):
        self.checker = 0
        self.pre = self.head
        for i in range(self.length):
            if newElement == self.pre.elem:
                self.checker = 1
            else:
                self.pre = self.pre.next
        if self.checker == 1:
            print(f"Key {newElement} already exists")
        else:
            if index == None:
                nxt = None
                new_node = Node(newElement, nxt)
                self.tail.next = new_node
                self.tail = new_node
                self.length += 1

            elif index == 0:
                self.pre = self.head
                new_node = Node(newElement,self.pre)
                self.head = new_node
                self.length += 1

            else:
                self.pre = self.head
                for i in range(index-1):
                    self.pre = self.pre.next
                new_node = Node(newElement,self.pre.next)
                self.pre.next = new_node
                self.length += 1




    def remove(self, deleteKey):
        self.x = self.head
        self.y = 0
        for i in range(self.length):
            if self.x.elem == deleteKey:
                self.y = 1
                break
            else:
                self.x = self.x.next
        if self.y == 0:
            print(f"Key {deleteKey} doesn't exist!")
        else:
            if self.length == 0:
                return None
            else:
                if self.head.elem == deleteKey:
                    self.x = self.head
                    self.head = self.x.next
                    self.x.next = None
                    self.length -= 1
                else:
                    self.pre = self.head
                    self.post = self.head.next
                    for i in range(self.length - 1):
                        if self.post.elem == deleteKey:
                            self.x = self.post
                            self.pre.next = self.x.next
                            self.x.next = None
                            self.length -= 1
                            break
                        else:
                            self.pre = self.post
                            self.post = self.post.next


    def evenList(self):
        lst = []
        x = self.head
        for i in range(self.length):
            if x.elem %2 == 0:
                lst.append(x.elem)
                x = x.next
            else:
                x = x.next
        y = LinkedList(lst)
        return y

    def find(self, element):
        self.finder = 0
        if self.length == 0:
            return None
        else:
            if self.head.elem == element:
                self.finder = 1
            else:
                self.pre = self.head
                self.post = self.head.next
                for i in range(self.length-1):
                    if self.post.elem == element:
                        self.finder = 1
                        break
                    else:
                        self.pre = self.post
                        self.post = self.post.next
        if self.finder==1:
            return True
        else:
            return False

    def reverseList(self):
        x = self.head
        self.head = self.tail
        self.tail = x
        after = x.next
        before = None
        for i in range(self.length):
            after = x.next
            x.next = before
            before = x
            x = after

    def sort(self):
        self.now = self.head
        self.value = None

        if (self.head == None and self.tail == None):
            print("EmptyList")
        else:
            for i in range(self.length):
                if self.now != None:
                    self.value = self.now.next

                    for j in range(self.length-1):
                        if self.value != None:
                            if (self.now.elem > self.value.elem):
                                x = self.now.elem
                                self.now.elem = self.value.elem
                                self.value.elem = x
                            self.value = self.value.next
                    self.now= self.now.next

    def sum(self):
        self.sum = 0
        if self.length == 0:
            self.sum = 0
        else:
            self.pre = self.head
            for i in range(self.length):
                self.sum+= self.pre.elem
                self.pre = self.pre.next

        return self.sum

    def rotateKTimes(self, k, direction):
        if direction == "left":
            for i in range(k):
                self.x = self.head
                self.tail.next = self.x
                self.head = self.x.next
                self.x.next = None
                self.tail = self.x
        if direction == "right":
            for i in range(k):
                self.x = self.head
                self.y = self.head
                for i in range(self.length):
                    if self.x.next == self.tail:
                        break
                    else:
                        self.x = self.x.next
                self.tail.next = self.y
                self.x.next= None
                self.head = self.tail
                self.tail = self.x


#==========================Tester Code==========================#

#Task-2.1, 2.2 -- Constructor & showList
print("\n//=======Task 2.1, 2.2 -- Constructor & showList=======//")
a = [10, 20, 30, 40, 50, 60]
l1 = LinkedList(a)
l1.showList() #Should print: 10->20->30->40->50->60

#Task-2.3 -- isEmpty
print("\n//========Task 2.3 -- isEmpty========//")
isListEmpty = l1.isEmpty()
print(isListEmpty) #Should print: false
b = []
l2 = LinkedList(b)
isListEmpty = l2.isEmpty()
print(isListEmpty) #Should print: true

#Task-2.4 -- Clear
print("\n//=======Task 2.4 -- Clear =======//")
print("Before clearing Linked List")
l1.showList() #Should print: 10->20->30->40->50->60
l1.clear()
print("After clearing Linked List")
l1.showList() #Should print: Empty List"""

#Task-2.5, 2.6 -- Insert
print("\n//=======Task 2.5, 2.6 -- Insert=======//")
c = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3 = LinkedList(c)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90
l3.insert(100)
l3.showList() #Should print: 10->20->30->40->50->60->70->80->90->100
l3.insert(0, 0)
l3.showList() #Should print: 0->10->20->30->40->50->60->70->80->90->100
l3.insert(110, 5)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100
l3.insert(120, 12)
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.insert(50) #Should print: Key 50 already exists"""

#Task-2.7 -- Remove
print("\n//=======Task 2.7 -- Remove=======//")
l3.showList() #Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(0)
l3.showList() #Should print: 10->20->30->40->110->50->60->70->80->90->100->120
l3.remove(110)
l3.showList()#Should print: 10->20->30->40->50->60->70->80->90->100->120
l3.remove(120)
l3.showList()#Should print: 10->20->30->40->50->60->70->80->90->100
l3.remove(120)#Should print: Key 120 does not exist

#Task-2.8 -- EvenList
print("\n//=======Task 2.8 -- EvenList =======//")
d = [1, 2, 5, 3, 8]
l4 = LinkedList(d)
l5 = l4.evenList()
l5.showList() #Should print: 2->8

#Task-2.9 -- Find
print("\n//=======Task 2.9 -- Find =======//")
found = l4.find(5)
print(found) #Should print: true
found = l4.find(4)
print(found) #Should print: false

#Task-2.10 -- Reverse List
print("\n//=======Task 2.10 -- Reverse =======//")
print("Before Reverse: ", end='')
l4.showList() #Should print: 1->2->5->3->8
l4.reverseList()
print("After Reverse: ", end='')
l4.showList() #Should print: 8->3->5->2->1

#Task-2.11 -- Sort
print("\n//=======Task 2.11 -- Sort =======//")
print("Before Sort: ", end='')
l4.showList() #Should print: 8->3->5->2->1
l4.sort()
print("After Sort: ", end='')
l4.showList() #Should print: 1->2->3->5->8

#Task-2.12 -- Sum of Elements
print("\n//=======Task 2.12 -- Sum of Elements =======//")
l4.showList() #Should print: 1->2->3->5->8
total = l4.sum()
print("Sum of Elements:", total)

#Task-2.13 -- Rotate
print("\n//=======Task 2.13 -- Rotate =======//")
l4.showList() #Should print: 1->2->3->5->8
l4.rotateKTimes(2, "left")
l4.showList() #Should print: 3->5->8->1->2
l4.rotateKTimes(2, "right")
l4.showList() #Should print: 1->2->3->5->8