#Linked_List
print('!!!!!!!LINKED LIST!!!!!!!')
def parenthesis_checker(val):
    stack = Stack(None)
    stack.pop()
    n = []
    for i in range(len(val)):
        if val[i] in "[{(":
            stack.push(val[i])
            n.append(i+1)
        if val[i] in "]})":
            x = stack.pop()
            for j in n:
                j=j
            if x == None:
                print(val)
                print(f"Error At character #{i+1}.{val[i]}- not opened")
                return
            elif val[i] == ")" and x in "[{":
                print(val)
                print(f"Error At character #{j}.{x}- is Not Closed")
                return
            elif val[i] == "}" and x in "[(":
                print(val)
                print(f"Error At character #{j}.{x}- is Not Closed")
                return
            elif val[i] == "]" and x in "{(":
                print(val)
                print(f"Error At character #{j}.{x}- is Not Closed")
                return
            else:
                n.pop()
    y = stack.pop()
    if y != None:
        print(val)
        print(f"{y} is not ended")
    else:
        print(val)
        print("This Expression is Ok")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node

    def print_stack(self):
        x = self.top
        while x!= None:
            print(x.value)
            x = x.next

    def push(self, value):
        x = self.top
        height = 0
        while x != None:
            height += 1
            x = x.next
        new_node = Node(value)
        if height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        height += 1
        return True

    def pop(self):
        x = self.top
        height = 0
        while x != None:
            height += 1
            x = x.next
        if height == 0:
            return None
        x = self.top
        self.top = self.top.next
        x.next = None
        height -= 1
        return x.value

parenthesis_checker("1+2*(3/4)")
parenthesis_checker("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
parenthesis_checker("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
parenthesis_checker("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")


#----------------------------------------------------------------------------------------------
#ARRAY
print("!!!!!!!!ARRAY!!!!!!!!")
def parenthesis_checker(val):
    stack = Stack()
    n = []
    for i in range(len(val)):
        if val[i] in "[{(":
            stack.push(val[i])
            n.append(i+1)
        if val[i] in "]})":
            x = stack.pointer
            for j in n:
                j=j
            if x>=0:
                m = stack.pop()
                if val[i] == ")" and m in "[{":
                    print(val)
                    print(f"Error At character #{j}.{m}- is Not Closed")
                    return
                elif val[i] == "}" and m in "[(":
                    print(val)
                    print(f"Error At character #{j}.{m}- is Not Closed")
                    return
                elif val[i] == "]" and m in "{(":
                    print(val)
                    print(f"Error At character #{j}.{m}- is Not Closed")
                    return
                else:
                    n.pop()
            else:
                print(val)
                print(f"Error At character #{i + 1}.{val[i]}- not opened")
                return
    z = stack.pointer
    if z >=0:
        y = stack.pop()
        print(val)
        print(f"{y} is not ended")
    else:
        print(val)
        print("This Expression is Ok")


class Stack:
    def __init__(self,value = None):
        self.stack = []
        self.pointer=-1
    def push(self, elem):
        self.stack.append(elem)
        self.pointer+=1
    def peek(self):
        return(self.stack[self.pointer])
    def pop(self):
        value = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer-=1
        return value



parenthesis_checker("1+2*(3/4)")
parenthesis_checker("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
parenthesis_checker("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
parenthesis_checker("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")

