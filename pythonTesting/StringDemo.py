str= "Shweta.com"
str1 = "Soft engg"
str3 = "Shweta"

print(str[1])  # output is "h"

print(str[0:5])   # if you want to get substring

print(str+str1)  # string concatenation

print(str3 in str)  # Substring check (want to check Shweta is present in "Shweta.com" or not)

var = str.split(".")  # split string
print(var)
print(var[0])

str4 = " great  "    # remove white spaces that is trim (in python for trip we use strip keyword
print(str4.strip())
print(str4.lstrip())  # remove left side spaces
print(str4.rstrip())   # remove right side spaces
