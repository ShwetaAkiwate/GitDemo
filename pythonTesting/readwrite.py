
file = open('test.txt')
# read all the contents of the file
#print(file.read(2))  # read n number of characters by passing parameter

# read one single line at a time readline()
# print(file.readline(2))
# print(file.readline(3))



# print lne by line using readline method
# line = file.readline()
# while line != "":
 #   print(line)
  #  line = file.readline()

# values = [abc, abc, bretwer, cere, derre, egrete]
for line in file.readlines():
    print(line)



file.close()