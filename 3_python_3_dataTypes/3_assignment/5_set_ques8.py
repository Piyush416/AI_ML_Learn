''' Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4] '''

list1 = [1, 2, 3]
list2 = [3,4]

set1 = set(list1)
set2 = set(list2)
print(type(set1))
res = set1.intersection(set2)
if res == set():
    print("No common")
else:
    print("have common element")
