#exercise 1
#Sum and average of a list

def load_vector():
    v = []
    r = 'y'
    while r == 'y' or r == 'Y':
        a = int(input("Enter a number: "))
        v.append(a)
        r = input("Do you want add new number? [Y/N]")
    print("Contents of the list:\n",v)
    return v


def sum_list(v):
    s = 0
    for elem in v:
        s += elem
    return s


def average(v):
    return float(sum_list(v)/len(v))


def main():

    v = load_vector()
    print("Sum: ",sum_list(v))
    print("Average: ",average(v))
    print()

main()


#exercise 2
#Inserting integer elements into a list
#a = number entered by user
#v = list
#r = sentinel variable

def orderly_insertion(v,a):
    if len(v) == 0 or v[-1] < a: # case 1 if len(v) is an empty list or 'a' is larger than the last element of list v
        v.append(a) # save value "a" at the end of the list "v"
    else:# otherwise it should be inserted in the middle or at the beginning
        i = 0
        while a > v[i] and i < len(v) - 1:# find the first position 'i' where 'a' is less than or equal to v[i].
            i += 1
        v.append(v[-1])# adds a dummy value at the end to make the list longer
        for j in range(len(v) - 2, i - 1, -1):
            v[j+1] = v[j]# move all items to the right
        v[i] = a# inserts the new value in the correct position
    print("After inserting",a,"v=",v)
    return v

def main():
    print("Ordered list insertion")
    v = []
    r = 'y'
    while r == 'y' or r == 'Y':
        a = int(input("Enter a number: "))
        v = orderly_insertion(v,a)
        r = input("Do you want to enter another number? [Y/N] ")

    print("Ordered list:",v)
    print()

main()

#exercise 3
#Sliding window

def load_vector():
    v = []
    r = 'y'
    while r == 'y' or r == 'Y':
        a = int(input("Enter a number: "))
        v.append(a)
        r = input("Do you want to enter another number? [Y/N] ")
    return v


def sliding_window(v):
    sw = []
    for i in range(1, len(v) - 1):
        sw.append((v[i-1]+ v[i] + v[i+1]) / 3.0)
    return sw

def main():
    v = load_vector()
    #v = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print("v =",v)
    if len(v) >= 3:
        sw = sliding_window(v)
        print("The result of applying the sliding window of width 3 is:")
        print(sw)
    else:
        print("Length of list lower than 3, sliding window not applicable")
    print()


main()


#exercise 4
#Sliding window in n size


def load_vector():
    v = []
    r = 'y'
    while r == 'y' or r == 'Y':
        a = int(input("Enter a number: "))
        v.append(a)
        r = input("Do you want to enter another number? [Y/N] ")
    return v


def sliding_window(v,n):
    sw = []
    for i in range(n//2, len(v) - n//2):
        sum = 0
        for j in range(i - n //2, i + n // 2 + 1):
            sum += v[j]
        sw.append(sum / float(n))
    return sw


def main():
    #v = load_vector()
    v = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    n = 2
    while n % 2 == 0:
        n = int(input("Enter sliding window size (odd number): "))
        print("v =",v)
    if len(v) >= n:
        sw = sliding_window(v,n)
        print("The result of applying the sliding window of width",n,"is:")
        print(sw)
    else:
        print("Length of list lower than ",n,"sliding window not applicable")
    print()


main()