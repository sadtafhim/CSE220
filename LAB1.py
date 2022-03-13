"""1. Shift Left k Cells
Consider an array named source. Write a method/function named shiftLeft( source, k)
that shifts all the elements of the source array to the left by 'k' positions. You must
execute the method by passing an array and number of cells to be shifted. After calling
the method, print the array to show whether the elements have been shifted properly.
Example:
source=[10,20,30,40,50,60]
shiftLeft(source,3)
After calling shiftLeft(source,3), printing the array should give the output as:
[ 40, 50, 60, 0, 0, 0]



Ans:"""


def shiftLeft(a, n):
    len_a = len(a)
    for count in range(n):

        for i in range(1, len_a):
            a[i - 1] = a[i]
        a[len_a - 1] = 0


source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)
print(source)

"""2.Consider an array named source. Write a method/function named rotateLeft( source, k)
that rotates all the elements of the source array to the left by 'k' positions. You must
execute the method by passing an array and number of cells to be shifted. After calling
the method, print the array to show whether the elements have been shifted properly.
Example:
source=[10,20,30,40,50,60]
rotateLeft(source,3)
After calling rotateLeft(source,3), printing the array should give the output as:
[ 40, 50, 60, 10, 20, 30]




Ans:"""


def rotateLeft(a, n):
    len_a = len(a)
    for count in range(n):
        x = a[0]

        for i in range(1, len_a):
            a[i - 1] = a[i]
        a[len_a - 1] = x


source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3)
print(source)

"""3. Remove an element from an array
Consider an array named source. Write a method/function named remove( source,
size, idx) that removes the element in index idx of the source array. You must execute
the method by passing an array, its size and the idx( that is the index of the element to
be removed). After calling the method, print the array to show whether the element of
that particular index has been removed properly.
Example:
source=[10,20,30,40,50,0,0]
remove(source,5,2)
After calling remove(source,5,2) , printing the array should give the output as:
[ 10,20,40,50,0,0,0]



ans:"""


def remove(a, n, x):
    for i in range(len(a)):
        if i == x:
            for j in range(x, len(a) - 1):
                a[j] = a[j + 1]

            a[len(a) - 1] = 0


        else:
            continue


source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 3)
print(source)

"""4. Remove all occurrences of a particular element from an array
Consider an array named source. Write a method/function named removeAll( source,
size, element) that removes all the occurrences of the given element in the source
array. You must execute the method by passing an array, its size and the element to be
removed. After calling the method, print the array to show whether all the occurrences
of the element have been removed properly.
Example:
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
After calling removeAll(source,7,2), all the occurrences of 2 must be removed. Printing
the array afterwards should give the output as:
[ 10,30,50,0,0,0,0,0,0]



ans:"""


def removeAll(s, o, n):
    m = o
    c = 0
    while m > 0:
        for i in range(m):
            if s[i] == n:
                for k in range(i + 1, len(s)):
                    s[k - 1] = s[k]
                    c += 1
                    s[len(s) - 1] = 0
            else:
                continue
        if c == 0:
            break
        m -= 1


source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source, 7, 2)
print(source)

"""5.Suppose the elements of an array A containing positive integers, denote the weights in
kilograms. And we have a beam balance. We want to put the weights on both pans of
the balance in such a way that for some index 0 < i < A.length - 1, all values starting
from A[0], A[1], upto A[ i - 1], should be on the left pan. And all values starting from A[ i ]
upto A[ A.length - 1] should be on the right pan and the left and right pan should be
balanced. If such an i exists, return true. Else, return false.
Input: [1, 1, 1, 2, 1] Output : true
Explanation: (summation of [1, 1, 1] = summation of [2,1])
Input: [2, 1, 1, 2, 1] Output: false


ans:"""


def balance(a):
    sum1 = 0

    x = False
    for i in range(len(a)):
        sum1 += a[i]
        sum2 = 0
        for j in range(i + 1, len(a)):
            sum2 += a[j]
        if sum1 == sum2:
            x = True
            break
        else:
            continue
    print(x)


balance([2, 1, 1, 2, 1])
"""6.Write a method that takes an integer value n as a parameter. Inside the method, you
should create an array of length n squared (n*n) and fill the array with the following
pattern. Return the array at the end and print it.
If,
n=2: { 0,1, 2,1 } (spaces have been added to show two distinct groups).
n=3 : { 0, 0, 1, 0, 2, 1, 3, 2, 1 } ((spaces have been added to show three distinct
groups).
n=4 : {0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1} (spaces have been added to show
four distinct groups).

ans:
"""


def array_series(num):
    size = num * num
    list1 = [0] * size

    x = 1
    while x <= num:
        y = 1
        while y <= x:
            list1[(x * num) - y] = y

            y += 1
        x += 1
    print(list1)


n = int(input())
array_series(n)

"""7. Max Bunch Count
A "bunch" in an array is a consecutive chain of two or more adjacent elements of the
same value. Write a method that returns the number of elements in the largest bunch
found in the given array.
Input: [1, 2, 2, 3, 4, 4, 4] Output: 3
Explanation: There are two bunches here {2,2} and {4,4,4}. The largest bunch is {4,4,4}
containing 3 elements so 3 is returned.
Input: [1,1,2, 2, 1, 1,1,1] Output:4
Explanation: There are three bunches here {1,1} and {2,2} and {1,1,1,1}. The largest
bunch is {1,1,1,1} containing 4 elements so 4 is returned.


ans:"""


def bunch(list):
    sum = 1
    max = 0
    for i in range(1, len(list)):
        if list[i] == list[i - 1]:
            sum += 1
            max = sum
        else:
            sum = 1
    print(max)


bunch([1, 2, 2, 3, 4, 4, 4])

"""8.
Write a method that takes in an array as a parameter and counts the repetition of each
element. That is, if an element has appeared in the array more than once, then its
‘repetition’ is its number of occurrences. The method returns true if there are at least
two elements with the same number of ‘repetition’. Otherwise, return false.
Input: {4,5,6,6,4,3,6,4} Output: True
Explanation: Two numbers repeat in this array: 4 and 6. 4 has a repetition of 3, 6 has a
repetition of 3. Since two numbers have the same repetition output is True.
Input: {3,4,6,3,4,7,4,6,8,6,6} Output: False
Explanation: Three numbers repeat in this array:3,4 and 6 .3 has a repetition of 2, 4 has
a repetition of 3, 6 has a repetition of 4. Since no two numbers have the same repetition
output is False.

Ans."""


def repetition(list):
    list2 = []
    dict = {}
    sumx = False
    for i in range(len(list)):
        if list[i] in list2:
            continue
        else:
            list2.append(list[i])
    for j in range(len(list2)):
        dict[list2[j]] = 0
    for k in range(len(list)):
        if list[k] in list2:
            dict[list[k]] += 1
        else:
            continue

    for m in range(len(list2)):
        if dict[list2[m]] != 1:
            x = dict[list2[m]]
            for n in range(m + 1, len(list2)):
                if dict[list2[n]] != 1:
                    if dict[list2[n]] == x:
                        sumx = True
                        break
                    else:
                        continue
                else:
                    continue
        else:
            continue
    print(dict)
    print(sumx)


repetition([4, 5, 6, 6, 4, 3, 6, 4])

"""9.Write a method/function that takes in a circular array, its size and start index and finds
whether the elements in the array form a palindrome or not. Return true if the elements
form a palindrome, otherwise, return false.
Example:
Input: [20,10,0,0,0,10,20,30] (start =5, size=5) Output: True.
Input:[10,20,0,0,0,10,20,30] (start =5, size=5) Output: False



Ans:"""


def palindrome(list1, v, w):
    x = False
    listx = []
    listy = []
    for i in range(1, len(list1)):
        if list1[i] == 0 and list1[i - 1] != 0:
            for j in range(i):
                listx.append(list1[j])

    for i in range(1, len(list1)):
        if list1[i] != 0 and list1[i - 1] == 0:
            for j in range(i, len(list1)):
                listy.append(list1[j])
    for k in range(1, len(listx)):
        for m in range(len(listy)):
            if listx[k] == listy[m] and listx[k - 1] == listy[m + 1]:
                x = True
                break
    print(x)


palindrome([20, 10, 0, 0, 0, 10, 20, 30], 5, 6)

"""10. Intersection
Write a method/function that takes two circular arrays, their sizes and start indexes and
returns a linear array containing the common elements between the two circular arrays.
Input:
Circular array 1 : [40,50,0,0,0,10,20,30] (start_1 =5, size_1 =5)
[10 20 30 40 50]
Circular array 2 : [10,20,5,0,0,0,0,0,5,40,15,25] (start_2=8, size_2 =7)
[5 40 15 25 10 20 5]
Output: [10,20,40]

ans"""


def palindrome(list1, v, w, list2, t, p):
    listw = []
    listx = []
    listy = []
    listz = []
    list_ult = []
    for i in range(1, len(list1)):
        if list1[i] == 0 and list1[i - 1] != 0:
            for j in range(i):
                listw.append(list1[j])

    for i in range(1, len(list1)):
        if list1[i] != 0 and list1[i - 1] == 0:
            for j in range(i, len(list1)):
                listx.append(list1[j])

    for i in range(1, len(list2)):
        if list2[i] == 0 and list2[i - 1] != 0:
            for j in range(i):
                listy.append(list2[j])

    for i in range(1, len(list2)):
        if list2[i] != 0 and list2[i - 1] == 0:
            for j in range(i, len(list2)):
                listz.append(list2[j])

    lista = listx + listw
    listb = listz + listy

    for i in range(len(lista)):
        x = lista[i]
        for j in range(len(listb)):
            if x == listb[j]:
                if x not in list_ult:
                    list_ult.append(x)
                else:
                    continue
            else:
                continue
    print(list_ult)


palindrome([40, 50, 0, 0, 0, 10, 20, 30], 5, 6, [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25], 8, 7)

"""11.Suppose you have been hired to develop a musical chair game. In this game there
will be 7 participants and all of them will be moving clockwise around a set of 7 chairs
organized in a circular manner while music will be played in the background. You will
control the music using random numbers between 0-3.If the generated random number
is 1, you will stop the music and if the number of participants who are still in the game is
n, the participants at position (n/2) will be eliminated. Each time a participant is
eliminated, a chair will be removed and you have to print the player names who are still
in the game.The game will end when there will be only one participant left. At the end of
the game,display the name of the winner.
[Hint: You will need to invoke a method to generate a random number between 0
(inclusive) to 3 (inclusive)]
Ans:"""

import random


def musical_chair(contestant):
    while len(contestant) > 1:
        print("Player Order:", contestant)
        randint = random.randint(0, 3)

        if randint == 1:
            if len(contestant) % 2 == 0:
                remove = int(len(contestant) / 2) - 1
            else:
                remove = int(len(contestant) / 2)
            print(f'player{remove} is out')
            contestant.pop(remove)
        contestant.insert(0, contestant[len(contestant) - 1])
        contestant.pop(len(contestant) - 1)
    print("Winner is", contestant[0])


list = [1, 2, 3, 4, 5, 6, 7]
musical_chair(list)