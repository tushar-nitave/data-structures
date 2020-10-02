from collections import deque

def disk_analysis(numComputer, segmentLength, hardDiskSpace):

    q = deque()
    result = []
    for i, value in enumerate(hardDiskSpace):
        while q and hardDiskSpace[q[-1]] >= value:
            q.pop()

        q.append(i)

        if q[0] == i-segmentLength:
            q.popleft()

        if i >= segmentLength-1:
            result.append(hardDiskSpace[q[0]])

    print(max(result))

disk_analysis(3, 2, [8, 2, 4])
