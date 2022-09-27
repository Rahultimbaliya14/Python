def linear_search(list, length,find):
    for i in range(0, length):
        if(list[i] == find):
            return i
    return -1 


list = [64, 34, 25, 12, 22, 11, 90]
length = len(list)
print(length)
target = int(input("which number : "))

position = linear_search(list, length, target)
if(position==-1):
    print("Not Found ",target)
else:
    print("found at " + str(position))