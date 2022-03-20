def Get_Mean_Method(previousMeanValue, newAngleValue):

    alpha = 2/(120+1)
    mean = previousMeanValue + alpha*(newAngleValue-previousMeanValue)

    return mean