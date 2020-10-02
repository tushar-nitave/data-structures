def lruCacheMisses(num, pages, maxCacheSize):

    cache = []
    cache_misses = 0

    for i in pages:
        # print(i)
        if i not in cache:
            cache_misses += 1
            if len(cache) == maxCacheSize:
                cache.pop(0)
            cache.append(i)
        else:
            cache.pop(cache.index(i))
            cache.append(i)
        # print(cache)
    return cache_misses

lruCacheMisses(6, [1,2,1,3,1,2], 2)


