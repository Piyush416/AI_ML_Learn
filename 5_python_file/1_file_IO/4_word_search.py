# search "Python" word in 4_word_search.txt file and print the line number. where it exits

with open("/Users/piyush/Desktop/Python/5_python_file/1_file_IO/4_word_search.txt", 'r') as f:
    line_no = 0
    while True:
        data = f.readline() # read line by line
        if data != "":
            line_no+=1
            if 'Python' in data:
                print(line_no)
                break
        else:
            print("Word Not Found")
            break
    