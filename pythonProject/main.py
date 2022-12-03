def buySell(arr):
    profit = 0
    numberOfTransictions = 0
    lastBoughtStockValue = 0
    numberOfLastBoughtLots = 0
    buy = True
    sell = False
    for i in range(len(arr)):
        if i != len(arr) - 1:
            if buy:
                if arr[i + 1] > arr[i]:
                    if numberOfTransictions == 0:
                        numberOfTransictions += 1
                        numberOfLastBoughtLots = 1
                        lastBoughtStockValue = arr[i]
                        buy =  False
                        sell = True
                        profit = -arr[i]
                    else:
                        numberOfTransictions += 1
                        numberOfLastBoughtLots = profit//arr[i]
                        lastBoughStockValue = arr[i]
                        profit = profit % lastBoughStockValue
                        buy =  False
                        sell = True
            elif sell:
                if arr[i] > arr[i + 1]:
                    numberOfTransictions += 1
                    profit += arr[i] * numberOfLastBoughtLots
                    buy = True
                    sell = False
        else:
            if sell:
                numberOfTransictions += 1
                profit += arr[i] * numberOfLastBoughtLots
                buy = True
                sell = False
    print("Maximized Profit: ",profit)

arr1 = [100, 50, 200, 400, 20, 60, 10, 90, 300, 200]
arr2 = [20, 30, 40, 10, 5, 80, 100, 60]
arr3 = [20, 10, 5, 30, 60, 90, 40, 50]
arr4 = [20, 5, 15, 35, 10, 50, 80, 40]

buySell(arr1)
buySell(arr2)
buySell(arr3)
buySell(arr4)

