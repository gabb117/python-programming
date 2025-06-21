#access to single caracter

#by for loop
string1 = "sun"
for a in string1:
    print((a))


string2 = "ramarro"
c = 0
for a in string2:
    if a == 'r' or a == 'R':
        c+=1
print("There are",c,"r in the string",string2)

#by index
print(string1[0],string1[1],string1[2])# first 3 words
print(string2[0],string2[1],string2[2])# first 3 words
print(string2[-3],string2[-2],string2[-1])# last 3 words
#[-1] last character
#[-2] second last character
#[-3] third last character

#print(string2[10])
#If the index is out of range an exception 'IndexError' will be raised
#to avoid exception use:
index = 10
if index < len(string2):
    print(string2[10])#print the last character if present
else:
    print("Invalid index")

#otherwise:
try:
    print(string2[10])
except:
    print("Invalid index")

#String Concatenation
s1 = "Hello Mario, "
s2 = "it's the hours "
s3 = str(20)
print(s1+s2+s3+":00")


#Portions of strings or substrings
s = "tonight is the night "
s1 = s[8 : len(s)]     #takes all letters from index 8 to the last index (last index is set manually as the maximum index)
s2 = s[8:]             #takes all letters from index 8 to the last index with maximum index set automatically
s3 = s[:7]             #takes all letters from first index to index seven
s4 = s[0 : len(s) : 2] #takes all letters from first to last index with a one-letter exclusion interval every printed letter

print("s1 = ",s1)
print("s2 = ",s2)
print("s3 = ",s3)
print("s4 = ",s4)
