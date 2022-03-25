
def Check_For_Peak(closePriceArray=[]):
    
    currentPrice = closePriceArray[len(closePriceArray)-1]

    # for price in closePriceArray:

    #     print("closingPriceArray in Peak.py: "+str(price))

    if(closePriceArray[7] < currentPrice and closePriceArray[4] < currentPrice and closePriceArray[1] < currentPrice):
        peak = True
    else:
        peak = False
    #print("currentPrice: {} - ".format(currentPrice)+str(peak))
    return peak