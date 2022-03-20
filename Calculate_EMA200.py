
def Get_NewestEMA200_Method(previousEMA200Value, newPrice):

    alpha = 2/(200+1)
    ema200Now = previousEMA200Value + alpha*(newPrice-previousEMA200Value)

    return ema200Now