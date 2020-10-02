def matchSecretLists(secretFruitList, customerPurchasedList):
    print(secretFruitList)
    print(customerPurchasedList)
    if (secretFruitList == None) or len(secretFruitList) == 0:
        return True
    if customerPurchasedList == None or len(customerPurchasedList) == 0:
        return False
    i = 0
    j = 0
    for k in range(len(customerPurchasedList)):
        if customerPurchasedList[k] == secretFruitList[i][j] or secretFruitList[i][j] == "anything":
            j += 1
            if j == len(secretFruitList[i]):
                j = 0
                i += 1
            if i == len(secretFruitList):
                return True
        else:
            if secretFruitList[i][0] == "anything":
                j = 1
            else:
                j = 0
    return False



print(matchSecretLists([['anything', 'apple'], ['banana', 'anything', 'banana']],
                       ['orange', 'grapes', 'apple', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana']))