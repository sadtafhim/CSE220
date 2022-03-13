class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None
head = Node(None)

class DoublyList:
    def __init__(self,a):
        if len(a)==0:
            self.head = head
            tail = head
        else:
            for i in range(len(a)):
                if i == 0:
                    new_node = Node(a[i])
                    self.head = head
                    head.next = new_node
                    tail = new_node
                    head.pre = tail
                    tail.next = head
                    tail.pre = head
                else:
                    new_node = Node(a[i])
                    tail.next = new_node
                    new_node.pre = tail
                    tail = new_node
                    head.pre = tail
                    tail.next = head

    def showList(self):
        if self.head.next == None:
            print("Empty List")

        else:
            count = 0
            m = self.head.next
            while m != self.head:
                if m.next == self.head:
                    print(m.data)
                    m = m.next
                    count += 1
                else:
                    print(m.data, end=" ")
                    m = m.next
                    count += 1

    def insert(self,newElement,index = None):
        m = self.head.next
        count = 0
        while m != self.head:
            count += 1
            m = m.next

        if index != None:
            if index > count or index<=0:
                print("Index Our of Bounds!")
            elif index == None:
                tail = self.head.pre
                new_node = Node(newElement)
                tail.next = new_node
                new_node.pre = tail
                self.head.pre = new_node
                new_node.next = self.head
            else:
                now = self.head
                post = now.next

                for i in range(index-1):
                    now = now.next
                    post = post.next

                new_node = Node(newElement)
                now.next = new_node
                new_node.pre = now
                new_node.next = post
                post.pre = new_node

    def remove(self,index):
        count = 0
        if self.head.next == None:
            print("Empty List")
        else:
            m = self.head.next
            while m != self.head:
                count+=1
                m = m.next
        if index <= 0 or index > count:
            print("Index Our of Bounds!")
        else:
            prev = self.head
            now = prev.next
            post = now.next
            for i in range(index-1):
                prev = prev.next
                now = now.next
                post= post.next

            prev.next = post
            post.pre = prev
    def removeKey(self,deletekey):
        count = 0
        counter = 0
        if self.head.next == None:
            print("Empty List")
        else:
            m = self.head.next
            while m != self.head:
                count += 1
                m = m.next
            now = self.head.next
            for i in range(count):
                if deletekey == now.data:
                    counter = 1
                    break
                else:
                    now = now.next
            if counter == 1:
                prev = self.head
                now = prev.next
                post = now.next

                for j in range(count):
                    if now.data == deletekey:
                        prev.next = now.next
                        post.pre = now.pre
                        now.pre = None
                        now.next = None
                        break
                    else:
                        prev = prev.next
                        now = now.next
                        post = post.next
            else:
                print(f"{deletekey} not in this list!")

arr = [1,2,3,4,5,6]
l1 = DoublyList(arr)
l1.showList()
l1.remove(2)
l1.showList()
l1.insert(7)
l1.showList()
l1.insert(2,2)
l1.showList()
l1.removeKey(6)
l1.showList()