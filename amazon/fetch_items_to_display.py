def fetch(numOfItems, items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    items.sort(key=lambda x:x[sortParameter], reverse=True if sortOrder else False)

    idx = 0
    result = []
    for i in range(0, numOfItems, itemsPerPage):
        page_items = items[i:i+itemsPerPage]

        if idx == pageNumber:
            for item in page_items:
                result.append(item)
        idx += 1
    return result

fetch(3, [["item1",10,15], ["item2",3,4], ["item3",17,8]], 1, 0, 2, 1)