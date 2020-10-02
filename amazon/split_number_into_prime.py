def isprime(n):
    print(n)
    n = int(n)
    if n<2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
MOD = 1000000007
def split_numbers(n, i):
    if (i==0):
        return 1

    count = 0

    for j in range(1,7):
        if i-j >0 and n[i-j] != "0" and isprime(n[i-j:j]):
            count += split_numbers(n, i-j)
        count %= MOD

    return count


print(split_numbers('11373', len('11373')))