import heapq

def max_profit_from_supplier(numSuppliers, inventory, order):
    max_profit = []
    profit = 0
    for price in inventory:
        heapq.heappush(max_profit, -price)
    while max_profit and order > 0:
        temp = heapq.heappop(max_profit)
        product= -temp
        profit += product
        if product > 0:
             product -= 1
        heapq.heappush(max_profit, -product)
        order -= 1
        print("Product:{} Heap:{} Profit: {}".format(product, max_profit, profit))
    print(profit)

max_profit_from_supplier(2,  [3, 5], 6)