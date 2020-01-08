def bubble_sort(array):
    print(array)
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(array)
if __name__ == "__main__":
    a = [5,2,1,4,7]
    bubble_sort(a)