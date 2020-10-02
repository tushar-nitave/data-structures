def get_neighbour(city,x,y, numOfCities, cities):
    idx = cities.index(city)
    finallist = []
    city_x = x[idx]
    city_y = y[idx]
    min_dist = 999999999999999999999
    dist = 0

    for i in range(numOfCities):
        if i != idx and (city_x == x[i] or city_y == y[i]):
            dist = abs(city_x-x[i])+abs(city_y - y[i])
            if dist < min_dist:
                finallist = []
                min_dist = dist
                finallist.append(i)
            elif dist == min_dist:
                finallist.append(i)
    return finallist


def findNearestCities(numOfCities, cities, x, y, numOfQueries, queries):
    result = []

    for idx, city in enumerate(queries):
        neighbour = get_neighbour(city,x, y, numOfCities, cities)
        if len(neighbour) == 0:
            result.append(None)
        elif len(neighbour) == 1:
            result.append(cities[neighbour[0]])
        else:
            temp = []
            for n in neighbour:
                temp.append(cities[n])
            result.append(sorted(temp)[0])
    return result

print(findNearestCities(6, ["green", "yellow", "red", "blue", "grey", "pink"], [10, 20,15,30,10,15], [30,25,30,40,25,25],4, ["grey", "blue", "red", "pink"]))