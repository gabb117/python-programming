#dictionary

if key in dictionary:
    del dictionary[key]
#search and delete key-value pair using "in" operator

try:
     del dictionary[key]
except KeyError:
    print("Key ",key," not present in dictionary")
#using exception to avoid error


dictionary = {'Mark':'1234', 'Maria':'5678', 'joe':'90123'}

print(len(dictionary))
#to know the number of elements (key-value pair) in a dictionary using len() function


for key in dictionary:
    print(key)
#print the keys contained in the dictionary

for key in dictionary:
    print(key,dictionary[key])
#print key-value pairs


#main methods of the dictionary object

dictionary = {'Mark':'1234', 'Maria':'5678', 'joe':'90123'}
print("Initialized dictionary: ",dictionary)


t = dictionary.items() #tuple
print("The variable t has dimension: ",len(t))
print(t)
#items() returns all keys and associated values ​​of the dictionary
#each element of t is a tuple containing an associated key-value pair

for tupla in t:
    print(tupla)
#iterate over tuples with for loop


k = dictionary.keys()
print(k)
for key in k:
    print(key)
#keys() method returns all the keys in the dictionary in sequence,only the keys but not the value.


values = dictionary.values()
print(values)
for val in values:
    print(val)
#returns all dictionary values ​​in a sequence, except dictionary keys


value = dictionary.pop(key,default)
#returns the value associated with a specific key and removes the key-value pair from the dictionary
# it also allows you to avoid the KeyError exception because if the key does not exist it returns default


pair = dictionary.popitem()
print("key-value pair extracted and deleted: ",pair)
#Picks a random value and removes it from the dictionary. 
#Useful for simulating card draws
#Returns a tuple


print("Mark: ",dictionary.get("Mark","Not found")) #print: 1234
print("Lisa: ",dictionary.get("Lisa","Not found")) #print: Not found
#Retrieves the value associated with a specific dictionary key,if it is not present it returns an error


dictionary.clear()
print("Dictionary after call to clear(): ",dictionary)
#clear() method deletes all key-value pairs leaving the dictionary completely empty