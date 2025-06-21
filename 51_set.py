#set

set1 = set(['a','b','c'])
set2 = set(['c','d','e'])
set3 = set(['c'])

string_set = set("abba")
print(string_set)


list1 = ["alpha","beta","gamma"]

set_list1 = set(list1)
print("Set contain: ",len(set_list1)," elements") #len() returns the number of elements in the set
print(set_list1)

set_list1.add("delta") #add a new element inside the set
print(set_list1) #the elements of the set are not ordered

new_set = set()
new_set.update(list1) #update() transfers elements of lists, strings or tuples into a set
print(new_set)

new_set.discard("alfa")
print("Remove alpha with discard") #This method does not throw exceptions
new_set.remove("alpha")
print("Remove alpha with remove") #This method throw exceptions

#mathematical concept of set: union and intersection
#union of two sets
set1.union(set2)
set1 | set2
#intersection of two sets
set1.intersection(set2)
set1 & set2

#difference between two sets
set1.difference(set2)
set1 - set2
#the elements of the first set that do not belong to the second set

#symmetric difference between two sets
set1.symmetric_difference(set2)
set1 ^ set2
#the elements not shared between the two sets

#subset
set1.issubset(set2)
set1 <= set2
#All elements of set1 are also included in set2

#superset
set1.issuperset(set2)
set1 >= set2
#set1 contains all the elements of set2

print("Union set1 and set2",set1 | set2)
print("Intersection set1 and set2",set1 & set2)
print("Difference set1 and set2",set1 - set2)
print("Symmetric difference set1 and set2",set1 ^ set2)
print("Set3 is subset of set2?",set3 <= set2)
print("Set1 is superset of set3?",set1 >= set3)

new_set.clear()
#delete all elements of the set