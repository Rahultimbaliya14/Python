def bubbleSort(list):
  for i in range(len(list)):
    for j in range(0, len(list) - i - 1):
      if list[j] > list[j + 1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp


list = [-2, 45, 0, 11, 55 , 26, 22, 0]

bubbleSort(list)

print('Sorted list in Ascending Order:')
print(list)