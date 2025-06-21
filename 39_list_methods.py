#list methods

def main():

    my_list = []

    for i in range(5):

        num = int(input("Enter "+str(i+1)+" value: "))

        while num in my_list:
            num = int(input("Enter "+str(i+1)+" value: "))

        my_list.append(num)#add an element to the list
        print(my_list)

    my_list.sort()#sorts items in ascending order
    print("Ordered list = ",my_list)

    my_list.reverse()#sorts items in descending order
    print("Reversed list = ",my_list)

    index = 4
    my_list.insert(index,1)#inserts an element at the indicated index position in the list
    print("List after insertion of element 1 in position 4 = ",my_list)

    my_list.remove(1)#remove an element inside the list
    print("List after removed element 1 = ",my_list)

    print("The third number at index 2 is: ",my_list.index(2))#Find the value corresponding to an index

   

#main()


#del instruction
#removes an element from a specific position
my_list = ['a','b','c','d','e']
print(my_list)
del my_list[2]#remove 'c' from the list
print(my_list)


#min() or max()
#return the minimum or maximum value of the list
list_num = [1,2,3,4,5]

print("Maximun value of the list: ",max(list_num))
print("Minimun value of the list: ",min(list_num))



#copy a list inside a new empty list
#solution 1
list_new = []
for elem in list_num:
    list_new.append(elem)
print(list_new)

#concatenate the old list to a new empty list
#solution 2
list_new = list()
list_new = list_new+list_num
print(list_new)