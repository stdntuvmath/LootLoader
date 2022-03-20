import math


def Return_Standard_Dev_of_Angle_of_EMA200(angleArray = []):
    
    
    #sigma = sqrt((difference^2+difference^2+...)/N)
    
    #find the mean
    #

    sumOfAnArray = sum(angleArray)

    mean = sumOfAnArray/120 #nowYourMessinWitha = sumOfAnArray

    differenceArray = []

    for eachAngle in angleArray:

        sqrOfDifference = (eachAngle - mean)**2
        differenceArray.append(sqrOfDifference)

    sumOfDifferences = sum(differenceArray)
    
    #sumOfSquares = sum(squareValueArray)
    average = sumOfDifferences/120
    standardDev_of_Angle = math.sqrt(average)

    return standardDev_of_Angle
