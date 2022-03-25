
def Check_For_Trough(closePriceArray=[]):
    
    currentPrice = closePriceArray[len(closePriceArray)-1]


    # for price in closePriceArray:

    #     print("closingPriceArray in Trough.py: "+str(price))

    if(closePriceArray[7] > currentPrice and closePriceArray[4] > currentPrice and closePriceArray[1] > currentPrice):
        trough = True
    else:
        trough = False
    #print("currentPrice: {} - ".format(currentPrice)+str(trough))

    return trough