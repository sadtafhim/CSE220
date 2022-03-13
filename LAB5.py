#Very_Easy
#a.
def factorial(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return a * factorial(a-1)

print(factorial(3))
print("-----")
#b.
def fibonacci(n,a=0,m=1):
  if n==0:
      return a
  else:
      x = a
      a = m
      m=x+m

      return fibonacci(n-1,a,m)

print(fibonacci(7))
print("-----")
#c.
def arrayPrinter(a):
    if a==[]:
        x = ""
        return x
    else:
        x = str(a[0])+","+arrayPrinter(a[1:])
        return x
print(arrayPrinter([1,2,3,4,5]))
print("-----")
#d.
def powerN(a,n):
    if n == 0:
        return 1
    else:
        return a * powerN(a,n-1)
print(powerN(3,0))
print(powerN(3,1))
print(powerN(3,2))
print(powerN(3,3))
print("-----")
#Easy
#a
def decimal_to_binary(decimal,binary=0):
    if decimal==1:
        return "1"
    elif decimal==0:
        return "0"
    else:
        binary = decimal%2
        binary = int(binary)
        if decimal%2==0:
            decimal = decimal/2
        elif decimal%2==1:
            decimal =decimal//2
    return decimal_to_binary(decimal,binary)+str(binary)

print(decimal_to_binary(43))
print("-----")
#b
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(None)

class DummyHeadedLinkedList:
    def __init__(self,a):
        if len(a)==0:
            self.head = head
            tail=head
        else:
            for i in range(len(a)):
                if i == 0:
                    new_node = Node(a[i])
                    self.head = head
                    self.head.next = new_node
                    tail = new_node
                else:
                    new_node = Node(a[i])
                    tail.next = new_node
                    tail = new_node

    def sum(self, node=head.next):
        if node == None:
            return 0
        else:
            return node.data + self.sum(node.next)

arr = [1,2,3,4,5,6]
l1 = DummyHeadedLinkedList(arr)
print(l1.sum(head.next))
print("-----")
#c
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DummyHeadedSinglylinkedlist:
    def __init__(self,a):
        for i in range(len(a)):
            if i==0:
                new_node = Node(a[i])
                self.head = new_node
                tail = new_node
            else:
                new_node = Node(a[i])
                tail.next = new_node
                tail = new_node

    def reverse(self,x):
        if x.next==None:
            print(x.data)
            return
        else:
            self.reverse(x.next)
            print(x.data)
    def showreversed(self):
        return self.reverse(self.head)
array = [1,2,3,4,5]
l1 = DummyHeadedSinglylinkedlist(array)
l1.showreversed()
print('-----')
#medium
def hocBuilder(height):
    if height==0:
        return 0
    elif height ==1:
        return 8
    else:
        return 5 + hocBuilder(height-1)\

print(hocBuilder(3))
print("-----")
#Hard
#a.
def pattern(a):
    def pattern_maker(x):
        if x == 1:
            return "1"
        else:
            return pattern_maker (x-1)+" "+ str(x)

    if a == 0:
        return ""
    else:
        x = pattern_maker(a)
        return pattern(a-1) + x + "\n"

print(pattern(5))
print("-----")
#b.
def pattern(a, l = 0):
    def pattern_maker(x):
        if x == 1:
            return " "*l+"1"
        else:
            return pattern_maker (x-1) +" "+ str(x)

    if a == 0:
        return ""
    else:
        x = pattern_maker(a)
        return pattern(a-1,l+2) + x + "\n"

print(pattern(5))
print("-----")
#very_hard
class FinalQ:
    def print(self, array, idx):
        if (idx < len(array)):
            profit = self.calcProfit(array[idx])
            print(str(idx + 1) + ". Investment: " + str(array[idx]) + "; Profit: " + profit)
            self.print(array, idx + 1)

    def calcProfit(self, investment):
        if investment <= 25000:
            return str(0.0)
        elif 25000<investment<10000:
            m = investment-25000
            n = m+m+m+m+(m/2)
            o = n/100
            return str(o)
        else:
            x = investment-100000
            m = 75000
            y = x + x + x + x + x + x + x + x
            n = m+m+m+m+(m/2)
            z = y / 100
            o = n / 100
            return str(o+z)
array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)
print("-----")