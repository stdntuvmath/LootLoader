import math



def CalculateAngle(currentEma200Value, previousEma200Value):

    value = currentEma200Value - previousEma200Value

    ema200Angle = math.atan(value * 180 / 3.14159)

    return ema200Angle
