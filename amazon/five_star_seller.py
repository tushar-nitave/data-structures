import heapq


def get_difference(product):
    current = product[0]/product[1]
    improved = (product[0]+1)/(product[1]+1)
    return improved-current


def fiveStartReviews(productRatings, ratingsThreshold):
    heap =[]
    times = 0
    # find the product which makes more difference in rating
    for idx, product in enumerate(productRatings):
        heapq.heappush(heap, (-get_difference(product), idx))

    while cal_percentage(productRatings) < ratingsThreshold:

        diff, idx = heapq.heappop(heap)

        productRatings[idx][0] += 1
        productRatings[idx][1] += 1

        new_product = [productRatings[idx][0], productRatings[idx][1]]
        heapq.heappush(heap, (-get_difference(new_product), idx))

        times += 1

    return times


def cal_percentage(productRatings):
    rating = 0
    for i in productRatings:
        rating += (i[0]/i[1])

    return rating*100 / len(productRatings)

print(fiveStarReviews([[4,4],[1,2],[3,6]], 77))
