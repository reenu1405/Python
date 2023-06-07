
# working with file
# this is the read mode
f = open("../../Desktop/open.txt", 'r')
# print(f.read()) # read full file at once
# Or
for line in f:
    print(line) # read file one by one
f.close() # make sure you close the file
# or
with open("../../Desktop/open.txt", 'r') as f:
    print(f.read()) # it will automatically open and  close the file
print(f.closed) # check if file is closed : will give  true

# this is the write mode
f = open("../../Desktop/open.txt", 'w')
print(f.write("this is first line in write mode"))
f.close()
# write function will overwrite all the existing content in file.


# this is the append mode
f = open("../../Desktop/open.txt", 'a')
print(f.write("\nthis is first line in write mode 2"))
f.close()
