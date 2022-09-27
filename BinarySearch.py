def binary_search(list, target, start, end):

    while(start < end):
        mid = int((start + end)/2)

        if(target == list[start]):
            return start

        if(target == list[end]):
            return end

        if(target == list[mid]):
            return mid
        elif(target < list[mid]):
            end = mid-1
        else:
            start = mid+1

    return -1



list = [64, 34, 25, 12, 22, 11, 90]
list.sort()
print(list)
length = len(list)

target = int(input("which number : "))

position = binary_search(list, target, 0, length-1)

print("found at " + str(position))