#regular expression = string with the description of a pattern

#'re' module
import re
# re.function(raw_pattern)
# compiled_pattern = re.compile(pattern, flags = 0)

#split() function
#split splits the string fragment into substrings based on the patterns set
# split(pattern, string, maxsplit = 0, flags = 0)
s = re.split(r"\W","Hello, world!")
print(s)
print()
#\W = all NON-alphanumeric characters, i.e. non-letters and non-numbers (e.g. spaces, punctuation, symbols).
#The 'r' prefix = indicates a raw string, meaning that Python interprets the regex characters literally (without special escapes).

string1 = "Today is a really beautiful day"
result = re.split('\s+', string1, 3)
print(result)
print()
#['Today', 'is', 'a', 'really beautiful day']
#the result will be a list split into three parts as required by the token

#Pattern = the regular expression (regex) used to indicate where to split the string.
#String = this is the string to split.
#Maxsplit (default: 0 → no limit) = limit the maximum number of splits (not the number of elements!).
#Flags = set extra options for the regex behavior, such as ignoring case, using multiline, etc.

#match() function
#checks if the beginning of a string matches the searched regex
#match(pattern, string, flags = 0)
#Returns the matching object if it matches, otherwise returns None if there is no match.
import re 
res1 = re.match(r"\d", "123, string starts with number")
print(res1)
print(res1.group())
#<re.Match object; span=(0, 1), match='1'> : searches for a starting number
#1 : group() returns the entire found fragment

res2 = re.match(r"\d+", "123, string starts with number")
print(res2)
print(res2.group())
#<re.Match object; span=(0, 3), match='123'> : search for more starting number becouse use \d+ and the string start with 3 numbers
#123 : return the entire found fragment

res3 = re.match(r"\d+", "String doesn't start with number")
print(res3)
print()
#None : returns None becouse the string doesn't start with numbers


import re
string1 = "Regular expressions - python programming"
result = re.match(r"regular", string1, re.I)
print(result)
print(result.group())
print()
#check that the string starts with the word "regular" regardless of case (uppercase or lowercase)

import re
string1 = "Regular expressions - python programming"
result = re.match(r".*", string1, re.I)
print(result)
print(result.group())
print()
#check that the string starts with any character regardless of case, print the string up to the end of the line

import re
string1 = "Regular expressions - python programming"
result = re.match(r".?", string1, re.I)
print(result)
print(result.group())
print()
#check that the string starts with a single character regardless of case, print the string up to the end of the line

import re
string1 = "329/1234567 phone number of Paolo Rossi"
result = re.match(r"\d{3}/\d{7}", string1, re.I)
print(result)
print(result.group())
print()
#verify that the string starts with a 3 digit phone number (320) followed by the slash character "/" and then another 7 digits (1234567)

import re
string1 = "329-1234567 phone number of Paolo Rossi"
result = re.match(r"\d{3}[- /]\d{7}", string1, re.I)
print(result)
print(result.group())
print()
#verify that the string starts with a 3 digit phone number (320) followed by the line character "-" and then another 7 digits (1234567)


#search() method
#search(pattern, string, flags = 0)
#Checks whether any part of a string matches the regular expression.
#Returns the corresponding object if found, otherwise None if not found

import re
string1 = "123456 : This string has at least one 1223 letter 1233456"
result = re.search(r"[a-z]+", string1, re.I)
print("Search function result:\n", result)
print("result.group() = ",result.group())
print()
result = re.search(r"[a-z]+",string1)
print("Search function result case sensitive", result)
print("result.group() = ",result.group())
print()
#search and pick the first word composed of letters ([a-z])
#in the first case including capital letters and in the second case excluding them

import re
string1 = "Python programming basics"
result1 = re.match(r"programming",string1,re.I)
result2 = re.search(r"programming", string1, re.I)
print("match result = ",result1)
print("search result = ",result2)
print("search result group() = ",result2.group())
print()
#first case: the match() function will not find the word "programming" because it is not at the beginning of the string.
#second case: the search() function will find the word "programming" because it will search inside the whole string.

import re
string1 = "Python programming basics"
result1 = re.search(r"^programming",string1,re.I)
result2 = re.search(r"^python", string1, re.I)
print("search programming result = ",result1)
print("search python result = ",result2)
print()
#with the ^ character indicating to search for the pattern at the beginning of the string, 
#we see that search() will behave like match()

import re
string1 = "Python programming basics"
result1 = re.search(r"^programming$",string1,re.I)
result2 = re.search(r"^python$", string1, re.I)
print("search programming result = ",result1)
print("search python result = ",result2)
print()
#with the $ character indicating to search at the end of the string.


import re
s = re.search("I", "Ciao")
print(s)
print()
#Output = None
#A capital I is searched for but it is not found
s = re.search("I", "Ciao", re.I)
print(s)
print()
#Output = <re.Match object; span=(1, 2), match='i'>
#The re.I flag allows us to ignore the difference between uppercase and lowercase letters, so the I will be found
s = re.search("I", "^Ciao", re.I|re.M)
print(s)
print()
#Output = <re.Match object; span=(2, 3), match='i'>
#The deI and re.M flags allow us to start from the beginning of the line (^) 
#and ignore the difference between uppercase and lowercase, so the I will be found

#findall() function
#finds all substrings that match the regular expression and returns a list of substrings, 
# if no match is found it returns an empty list.
#findall(pattern, string, flags = 0)

import re
string1 = "123456 : This string has at least one 1223 letter 1233456"
result = re.findall(r"[a-z]+", string1, re.I)
print("Findall function result:\n", result)
#Findall function result finds all lowercase letter:
# ['This', 'string', 'has', 'at', 'least', 'one', 'letter']
print() 
result = re.findall(r"[a-z]+", string1)
print("Findall function result case sensitive:\n", result)
print()
#Findall function result case sensitive finds all letter:
# ['his', 'string', 'has', 'at', 'least', 'one', 'letter']

import re
string1 = 'class = "pluto" id = "pippo"'
result = re.findall(r'".*"', string1,re.I)
print(result)
print()
#['"pluto" id = "pippo"']
#.* finds all words enclosed in quotes but not correctly, including unwanted words

import re
string1 = 'class = "pluto" id = "pippo"'
result = re.findall(r'".*?"', string1,re.I)
print(result)
print()
#['"pluto"', '"pippo"']
#The ? sign helps you locate the letters you searched for correctly, including comma for separate every letter


#finditer() function
#also returns the index along with the matching strings
#finditer(pattern, string, flag)
#start(): returns the initial index of the match found
#end(): returns the final indexx of the match found
#group(): returns the match found

import re
string1 = "I go to the beach 4 hours a day. I walk 2 hours a day."
pattern = r"[0-9]"
for result in re.finditer(pattern,string1):
    s = result.start()
    e = result.end()
    g = result.group()
    print(g,"found in position [",s,",",e,"]")
    print()
# Output: 4 found in position [ 18 , 19 ]
# Output: 2 found in position [ 40 , 41 ]


#sub() function
#replaces all matching non-overlapping parts of a string with a substitute

#sub(pattern, substitute, string, flags = 0)
#subn() returns also the number of substitutions

import re
string1 = "123456 : This string has at least one 1223 letter 1233456"
result = re.sub(r"[A-Za-z]+", "[...]", string1)
print("Sub() function result:\n",result)
print()
#Sub() function result:
# 123456 : [...] [...] [...] [...] [...] [...] 1223 [...] 1233456

#pre-filled pattern
import re
pre_filled_pattern = re.compile(r"\d+")
#returns every numeric cypher one or more times
res1 = pre_filled_pattern.search("Lalalala 123")
print(res1)
print(res1.group())
#<re.Match object; span=(9, 12), match='123'>
#123

res2 = pre_filled_pattern.search("234Lalalala 123456789")
print(res2)
print(res2.group())
print()
#<re.Match object; span=(0, 3), match='234'>
#234


#Assertion : lookahed positive = (?=pattern)
import re
string1 = "Paolo Rossi Paolo Verdi Paolo Bianchi"
res1 = re.findall(r"Paolo", string1, re.I)
print(res1)
#['Paolo', 'Paolo', 'Paolo']
#find every Paolo present in the string

string1 = "Paolo Rossi Paolo Verdi Paolo Bianchi"
res2 = re.findall(r'Paolo (?=Rossi)', string1, re.I)
print(res2)
print()
#['Paolo ']
#find only one specific Paolo (Rossi)

#Assertion : lookbehind positive = (?<=pattern)
import re
text = "cesto pasto fasto pesto costo"
result = re.findall(r"(\w+(?<=a)sto)", text)
print(result)
#['pasto', 'fasto']
#check all words ending with "sto" whose preceding letter is "a"

#Assertion: lookbehind negative = (?<!pattern)
import re
text = "cesto pasto fasto pesto costo"
print(re.findall(r"(\w+(?<!a)sto)", text))
print()
#['cesto', 'pesto', 'costo']
#check all word ending with "sto" whose preceding letter is not "a"


#Repetition of groups of words or numbers
import re
p = re.compile("(ab)*")
print(p.match("abababababababab"))
print()

#Gruops with () capture starting and ending of text's index 
import re
p = re.compile("(a)b")
m = p.match("ab")
print(m.group())
print(m.group(0))#returns the entire match, that is "ab".
print(m.group(1))#returns the first group in parentheses, that is "a".
print()

#Subgroups with nested parentheses
p = re.compile("(a(b)c)d")
m = p.match("abcd")

print(m.group(0))#returns the entire match, that is "abcd".
print(m.group(1))#returns the letter in the first 2 parenthesis
print(m.group(2))#returns the letter in the most nested parenthesis

print(m.group(2,1,2))
print()
#('b', 'abc', 'b')
#returns a tuple plus values ​​corresponding to the group at once

print(m.groups())
print()
#('abc', 'b')
#returns a tuple with the string of all subgroups, from 1 onwards

import re
p = re.compile(r"(\b\w+)\s+\1")
print(p.search("RE founded inside inside the string").group())
print()
#Output: inside inside
#Search for a word, followed by spaces, followed by the exact same word,that is, look for double words

import re
p = re.compile(r"(?P<word>\b\w+\b)")
m = p.search("(((Lots of punctuation)))")
print(m.group("word"))
print(m.group(1))
print()
#Output: Lots
#        Lots
#(?P<word>...) defines a named group called "word"
#\b word boundary
#\w+ one or more alphanumeric characters (a word)
#So the pattern captures a word at the beginning, in this case "Lots"


import re
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)") 
result = p.search("RE founded inside inside the string")
print(result)
print(result.group())
print()
#<re.Match object; span=(11, 24), match='inside inside'>
#inside inside
#Find two consecutive identical words


import re

string1 = "This is a portion of text -- with punctuation."

for pattern in [r"^(?P<first_word>\w+)",r"(?P<last_word>\w+)\S*$",r"(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)",r"(?P<end_with_o>\w+o)\b"]:
    compiled_pattern = re.compile(pattern)
    match = compiled_pattern.search(string1)
    print("Correspondence",pattern)
    #print("Groups:",match.groups())
    print()



#group without capture
import re
m = re.match("([abc])+","abc")#([abc]) capture group
print(m)
print(m.groups())
#<re.Match object; span=(0, 3), match='abc'>
#('c',)

m = re.match("(?:[abc])+", "abc")#([abc]) group without capture
print(m)
print(m.groups())
print()
#<re.Match object; span=(0, 3), match='abc'>
#()


#exercise 1 - 2
import re
text = "cane crotalo canarino criceto cervo daino dromedario"
print(re.findall(r"\b(c(?=[aeiou])\w+)", text))
print()
#Finds words starting with the letter "c" only if followed by a vowel
#['cane', 'canarino', 'cervo']
print(re.findall(r"\b(c(?![aeiou])\w+)", text))
print()
#Finds words starting with the letter "c" only if not followed by a vowel,but followed by consonants
#['crotalo', 'criceto']

#exercise 3
#date replacement from italian to american format
import re
text = " 31-01-10_photo32 \n 24-01-10_photo1 \n 24-02-10_photo_monia \n 11-03-09_photo_lisa"

print("Text with format date dd-mm-yyyy:\n" + text)

text = re.sub(r"(?P<dd>\d{2})-(?P<mm>\d{2})-(?P<yyyy>\d{2})_photo(?P<final>.*)",r"\2-\1-20\3_photo\4", text)

print("text with format date mm-dd-yyyy:\n",text)
#   (?P<dd>\d{2}) → day
#	(?P<mm>\d{2}) → month
#	(?P<yy>\d{2}) → short year
#	_photo → fixed part
#	(?P<suffix>\S*) → everything that comes after _photo, without spaces


#exercise 4
#verify an e-mail address in shape "user_name@domain.com"
import re

email = "dz@domain.aa.com az@domain.com @domain.it cz@ cz@domain"
token = email.split(' ')
pattern = r"[a-zA-Z][\w-]*@[a-zA-Z]+(\.[a-z]{2,3})+"
for string1 in token:
    print(string1,end=' - ')
    result = re.search(pattern,string1)
    if result:
        print("Valid email!")
    else:
        print("invalid email!")

