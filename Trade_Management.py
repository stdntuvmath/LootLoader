

def Get_Profit(buyPrice, sellPrice, accountValue):

    profit = 0
    #take from the accountValue your riskAmount

    # if (buyPrice <= 3.00):
    #     risk = buyPrice*1000
    
    # if (buyPrice > 3.00 and buyPrice <= 30.00):
    #     risk = buyPrice*100

    # if (buyPrice > 30.00):
    #     risk = buyPrice*10   




    if (buyPrice <= 3.00):
        profit = (sellPrice - buyPrice)*1000
    
    if (buyPrice > 3.00 and buyPrice <= 30.00):
        profit = (sellPrice - buyPrice)*100

    if (buyPrice > 30.00 and buyPrice < 300.00):
        profit = (sellPrice - buyPrice)*10

    accountValue = accountValue + profit

    return accountValue