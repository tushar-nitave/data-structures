
def sort(a, p, n):
    if p < n:
        q = (p+(n-1))//2
        sort(a, p, q)
        sort(a, q+1, n)
        merge(a, p, q, n)
        

def merge(a, p, q, r):
    print(a, p, q, r)
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(n1):
        L.append(a[p+i])
    for i in range(n2):
        R.append(a[q+i+1])
    i = 0
    j = 0
    k = p
    print(L," ",R)
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i = i+1
        else:
            a[k] = R[j]
            j = j+1
        k = k+1
    while i < n1:
        a[k] = L[i]
        i = i+1
        k = k+1
    while j < n2:
        a[k] = R[j]
        j = j+1
        k = k+1
    print("After merge: ", a)
if __name__ == "__main__":
    a = [5, 3, 2, 4, 8, 1]
    sort(a, 0, len(a)-1)
    print(a)