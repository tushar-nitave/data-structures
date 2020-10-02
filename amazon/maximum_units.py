import heapq


def max_units(num, boxes, unitSize, unitsPerBox, truckSize):

    heap = []

    for i in range(len(boxes)):
        units_per_box = unitsPerBox[i]
        heapq.heappush(heap, (-units_per_box, boxes[i]))

    result = 0

    for i in heap:
        print(i)
    while truckSize > 0:
        current_max = heapq.heappop(heap)
        max_boxes = min(truckSize, current_max[1])
        truckSize -= max_boxes
        result += max_boxes * (current_max[0]*-1)

    print(result)

max_units(3, [1, 2, 3], 3, [3, 2, 1], 3)