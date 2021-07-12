
values = [1, 2, "Krunal", 4, 5]

# list is data type  that allows multiple values and can be different data type

print(values[0])

print(values[3])

print(values[-1])  # if you want to print last value in the list. this is shortcut

print(values[1:3])

values.insert(3, "shweta")

print(values)

values.append("End")
print(values)

values[2] = "KRUNAL"  # update values

del values[0]  #[2, 'KRUNAL', 'shweta', 4, 5, 'End']

print(values)

# Tuple - same as list data type, but immutable where updation is not possible
#val = (1, 2, "SHWETA", 4.5)
#print(val[1])

#val[2] = "shweta"

#print(val)

# dictionary

dic = {"a" : 2, 4 : "shweta", "c" : "Hello world"}
print(dic[4])
print(dic["c"])

# how to create dictionary at run time and add data into it
dict = {}

dict["firstname"] = "Krunal"
dict["lastname"] = "Intwala"
dict["gender"] = "Male"

print(dict)
print(dict["lastname"])
