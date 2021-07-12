
it = 10

while it > 1:
    #if it != 3:  #skipping value 3
    #if it == 3:  # breaks while loop
        #break
    if it == 9:
        it = it - 1  # it will not print value 9 in output
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print("while loop execution is done")