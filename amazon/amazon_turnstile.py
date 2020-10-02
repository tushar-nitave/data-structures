from collections import deque


def getTimes(numCustomers, arrTime, direction):
    enter = deque()
    exit = deque()

    time = 0
    status = True
    result = [-1]*numCustomers
    i = 0

    while i < numCustomers or enter or exit:
        while i < numCustomers:
            if direction and direction[i] == 0:
                enter.append(i)
            else:
                exit.append(i)
            i += 1
        if enter or exit:
            if exit and status:
                result[exit.popleft()] = time
            elif enter and not status:
                result[enter.popleft()] = time
            elif exit:
                result[exit.popleft()] = time
                status = True
            elif enter:
                result[enter.popleft()] = time
                status = False
        else:
            status = True
            time = arrTime[i] - 1
        time += 1
    return result


print(getTimes(100, [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 15, 18, 18, 18, 18, 19, 21, 22, 22, 23, 24, 25, 27, 27, 28, 28, 28, 28, 29, 30, 30, 30, 31, 32, 32, 32, 33, 33, 33, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 42, 42, 43, 44, 45, 45, 45, 46, 46, 48, 48, 49, 49, 50, 50, 50, 50],
         [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1]))