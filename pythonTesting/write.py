# read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('test.txt', 'r') as reader: # with is used for open the file, shortcut of "file = open('test.txt') file.close())"
    content = reader.readlines()   #[abc,bretwer,cere, derre,egrete]
    reversed(content)   #[egrete,derre,cere,bretwer,abc]
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)

