#python list

list_num = [1,2,3,4,5]
list_str = ["green","yellow","blue","red"]
list_mix = [1,"red","blue",4,5]
#a list can contain different data types
print(list_num)
print(list_str)
print(list_mix)

#repetition operator
list_zero = [0] * 5 
#create multiple copy of the same element inside the list 
list_binary = [0,1,"blue"] * 5
#create multiple copy of different elements inside the list

print(list_zero)
print(list_binary)


#object iteration with loop for
list_num = [1,2,3,4,5]

for x in list_num:
    print("Element: ",x)


#indexing list
#index start from 0 to n
print(list_num[3]) #4
print(list_mix[2]) #blue
print(list_num[-1]) #5 index of last element of the list
print(list_num[-2]) #4 index of second last element of the list


#list length
l = len(list_num)
print("List length is: ",l," characters")


#to avoid IndexError use:
i = 10
if (i < len(list_num)):
    print(list_num)
else:
    print("Incorrect index. List size = ", len(list_num))

#or

i = 10
try:
    print(list_num[i])
except IndexError:
    print("Incorrect index. List size = ", len(list_num))


#mutable sequence
#inserts ten elements into the list adding the counter at each iteration
def main():
    count = [0] * 10

    for i in range (10):
        count[i] = i + 1
    print(count)

main()


#how to create a not tidy list of 10 elements
def counter ():
    count = [0] * 10 # 10 is the size of list

    for i in range(10):
        count[i] = int(input("Enter "+str(i+1)+"° element:"))

    print(count)

counter()


#how to create a list of even number 
def list_even():
    count = [0] * 10 #10 is the list size

    for i in range (10):
        count[i] = (i+1) * 2
        
    print(count)

list_even()


#concatenate two different lists
def list_conc():
    
    list_1 = ['a','b','c','d','e']
    list_2 = [1,2,3,4,5,6,7,8]

    list_tot = list_1 + list_2
    print(list_tot)

list_conc()



#sublist or slice
list_1 = ['a','b','c','d','e']
start = 2 #the start range (inclusive value) 
end = 4 # the end range (excluding value)

sublist = list_1[start:end]
print("Slice =", sublist)



#operator 'in', element in list
#How to know if a certain element is present in the list
def party():
    guest_list = ["Fabio","Francesca","Valerio","Giovanna","Gabriele"]
    
    name = input("Enter a guest name: ")

    if name in guest_list:
        print(name,": he/she is among the guests")
    else:
        print("he/she is not among the guests")

party()