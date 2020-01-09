def quicksort(array, l, r):
    i = l
    j = r
    pivot = array[(l+r)//2]

    while i <=j:

        while array[i] < pivot:
            i = i+1
        while array[j] > pivot:
            j = j-1
    
        if i <= j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i = i+1
            j = j-1
          

    if l<j:
        quicksort(array, l, j)
    if i<r:
        quicksort(array, i, r)
    

if __name__ == "__main__":
    array = [1,3,6,2,5,8,7]
    quicksort(array, 0, len(array)-1)
    print(array)