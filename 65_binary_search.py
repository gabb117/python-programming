#binary search

# v: a list sorted in ascending order.
# x: the value we want to search for in the list.
# a: average index between low and up
def binary_search(v,x):
    n = len(v) # list length
    low = 0 # start of search range (lowest index)
    up = n - 1 # end of search range (highest index)
    if x < v[low] or x > v[up]: 
    #If 'x' is smaller than the first element or larger than the last, it cannot be present (because the list is sorted).
        return -1 #Returns -1 to indicate that it did not find the element
    while low <= up:
        a = (low + up) // 2 #is the average index between 'low' and 'up'. 
        if v[a] == x: #The central element is 'v[a]'.
            return a  #if central element is what we are searching, it returns the average index 
        if x > v[a]: #If 'x' is larger than the center element, we search the right half.
            low = a + 1 #Update low to the next value after a.
        else:           #If 'x' is smaller than the center element, we search the left half.
            up = a - 1. #Update 'up' to the value before m.
    return -1 #If the loop exits without finding 'x', then the element is not present.


def main():
    v = [1,4,5,6,7,8,9,10,11,12,13,15,18,19]
    print(v)

    r = 'y'
    while r == 'y' or r == 'Y':
        x = int(input("Enter search number: "))
        i = binary_search(v,x)
        if i != -1: #if function doesn't return -1 value, number will be insiede the list
            print("Number chosen",x,",founded at position",i)
        else: #if function returns -1 value, number will not be in list
            print("Number not found")
        r = input("Do you want to search for another number [Y/N] ?")

main()