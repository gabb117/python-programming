#Test,search and manipulation

names = "Antonio Barbara Carlo Deborah Fabio Giorgia"
n = input("Enter a name to search, use capital letter for first letter : ")
if n in names:
    print(n," it's in the list")
else:
    print(n,"it's not in the list")


#String methods:
# isalnum() = True if string contains only alphanumeric characters and his length is >= 1.
# isalpha() = True if string contains only alphabetical characters and his length is >= 1.
# isdigit() = True if string contains only numeric characters and his length is >= 1.
# islower() = True if string contains all lowercase alphabetic characters and his length is >= 1.
# isupper() = True if string contins all uppercase alphabetic characters and his length is >= 1.
# isspace() = True if string contains only whitespaces (space, \n, \t) and his length is >= 1.

s = "abracadabra" 
if s.islower():
    print(s,"contains all lowercase characters.")
s = "ABRACADABRA"
if s.isupper():
    print(s,"contains all uppercase characters.")
s = "3nights"
if s.isalnum():
    print(s,"Contains both alphabetic and numeric characters.")
if s.isalpha():
    print(s,"Contains only alphabetic characters.")

#methods for string modify:
# lower() = returns string with all lowercase characters
# upper() = returns string with all uppercase characters
# lstrip() = returns string with all leading whitespace removed (space, \n, \t)
# rstrip() = returns string with all final whitespace removed (space, \n, \t )
# strip() = returns string with all leading an final whitespace removed (space, \n, \t)
# lstrip(c), rstrip(c), strip(c) = returns string with all the indicated leading or final or both whitespace removed 

s = " x hello x "
print("Original string \t|",s,"|",sep="")
print("upper \t\t|",s.upper(),"|",sep="")
print("lstrip \t\t|",s.lstrip(),"|",sep="")
print("rstrip \t\t|",s.rstrip(),"|",sep="")
print("strip \t\t|",s.strip(),"|",sep="")
print("lstrip \t\t|",s.lstrip("x "),"|",sep="")


#All methods for serching and Substring replacement in larger strings

# endswith(substring) = True if string ends with substring.
# starsswith(substring) = True if string starts with substring.
# find(substring) = returns the index of the first character of the substring in the string, if not present returns -1.
# replace(old,new) = returns a copy of string with old character is replaced by new character.

filename = input("Enter file name: ")
if filename.endswith(".txt"):
    print("Text file")
elif filename.endswith(".py"):
    print("Python file")
else:
    print("Unknown file type")


string = """Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura, chè la diritta via era smarrita."""
subs = "vita"
i = string.find(subs)
if i == -1:
    print("Word",subs,"not found")
else:
    print("First occurence of word",subs,"founded in index",i)# it find the word at 31 index of phrases.

subs = "cammin"
print(string.replace(subs,"cammin"))# replace word "cammino" with "cammin"


string = "a" * 5
print(string)
 

for i in range(1,5):
    print("a" * i)
for i in range(5,0,-1):
    print("a" * i)


#split method
# returns a list containing the words in the string separated by spaces or other characters ("/")

s = """Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura, chè la diritta via era smarrita."""
print(s.split())

d = "01/08/2021"
print(d.split("/"))

#join method
# joins lists of strings to form a single string object

list1 = ["ciao","house","sea","montain"]
s = ", "  #if we combine a variable s with the "," sign to the method we get a separator for each element of the list
print(s.join(list1))


#combined use of join() and split() allows you to remove unwanted spaces from a string

string1 = "There are\t random spaces\t in this string "
s = " "
print(s.join(string1.split()))


