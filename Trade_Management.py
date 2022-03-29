

def Get_Risk_Amount(buyPrice):

    profit = 0
    #take from the accountValue your riskAmount

    if (buyPrice <= 3.00):
        risk = buyPrice*1000
    
    if (buyPrice > 3.00 and buyPrice <= 30.00):
        risk = buyPrice*100

    if (buyPrice > 30.00 and buyPrice <=300):
        risk = buyPrice*10   

    return risk


def Get_Share_Amount(buyPrice):

    profit = 0
    #take from the accountValue your riskAmount

    if (buyPrice <= 3.00):
        shareAmount = 1000
    
    if (buyPrice > 3.00 and buyPrice <= 30.00):
        shareAmount = 100

    if (buyPrice > 30.00 and buyPrice <=300):
        shareAmount = 10   

    return shareAmount