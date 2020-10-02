from collections import Counter


def processLogFile(logs, threshold):
    freq = []
    result = []
    for i in logs:
        sender, receiver, _ = i.split(" ")
        if sender != receiver:
            freq.append(sender)
            freq.append(receiver)
        else:
            freq.append(sender)
    transaction = Counter(freq)
    freq=[]
    for i in transaction.items():
        freq.append(list(i))
    print(freq)
    freq.sort(key=lambda x:x[1], reverse=False)

    for i in freq:
        if i[1] >= threshold:
            result.append(i[0])
    return result


processLogFile(['88 99 200', '88 99 300', '99 32 100', '12 12 15'], 1)