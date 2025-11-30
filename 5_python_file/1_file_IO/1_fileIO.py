# learnig file operators

# there are three step to perform file operation
# 1. open file using open() function
# 2. perform operation like reading or writing in the file
# 3. close the file

# # open file
# f = open("/Users/piyush/Desktop/Python/5_python_file/1_file_IO/sample.txt", 'r') # open function will return the file object.

# # perform operation
# data = f.read()
# print(data)

# # close file
# f.close()


# --------------------------------------------------------

# Types of mode 
# 1. r -> reading [default]
# 2. w -> writing, (truncate/clear) file first , if file not exit create it 
# 3. x -> create new & open for writing
# 4. a -> writing, append at end
# 5. b -> binary mode -> use in image and video that store in binary formate
# 6. t -> text mode [default]
# 7. + -> opens disk file for update(r & w)


# --------------------------------------------------------
# difference between w and x 
# x -> if file is exit then it will not truncate it give error file is exit
# w -> without any error clear a file and over write it 

# using x mode
# f = open("/Users/piyush/Desktop/Python/5_python_file/1_file_IO/sample1.txt", 'x')
# data = f.write("shree saini pb")
# print(data) # output is the length of string.
# f.close()

# using w mode
# f = open("/Users/piyush/Desktop/Python/5_python_file/1_file_IO/sample.txt", 'w')
# data = f.write("shree saini")
# f.close()

# --------------------------------------------------------

# r -> read , rb -> read_binary , w-> write , wb -> write_binary

# --------------------------------------------------------

# + mode we can use it with r and w
# r+ -> read file and write at the file
# w+ -> write file and read the data
# a+ -> write the file and read the file

# what is difference between r+ , w+, a+
# r+ -> in 'r' we have pointer at the start so we can do read/write at the start.
# a+ -> in 'a' we have pointer at the end so we can do read/write at the end. and read is also start from the end.
# w+ -> in 'w' we first truncate/clear the file first and then read/write the file.


# r+ mode understanding with example
''' 
Hello My name is Piyush
I am learning Python
and File IO operation '''  # this text is paste in sample.txt

# if we use 'r+' at the starting in sample.txt we can write and read file 
# f = open("/Users/piyush/Desktop/Python/5_python_file/1_file_IO/sample.txt", 'r+')
# f.write("1234")
# print(f.read())
# f.close()
'''  -> "Hello" is replace with "1234"
1234 My name is Piyush
I am learning Python
and File IO operation '''  # this text is present in sample.txt

''' 
My name is Piyush
I am learning Python
and File IO operation '''  # this text will get in console

# --------------------------------------------------------------------------------

# f = open("/Users/piyush/Desktop/Python/5_python_file/1_file_IO/sample.txt", 'w+')
# # after this line file will be truncate

# print(f.read()) # empty
# f.write("Hello Piyush")
# f.close()

# --------------------------------------------------------------------------------

# mode_chat to understand which mode we have to use 
