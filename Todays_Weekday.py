import datetime

def Get_Todays_Weekday_Name():

    todaysNumberAccordingToPython = datetime.datetime.today().weekday()

    if(todaysNumberAccordingToPython == 0):
        return str("Monday")
    elif(todaysNumberAccordingToPython == 1):
        return str("Tuesday")
    elif(todaysNumberAccordingToPython == 2):
        return str("Wednesday")
    elif(todaysNumberAccordingToPython == 3):
        return str("Thursday")
    elif(todaysNumberAccordingToPython == 4):
        return str("Friday")
    elif(todaysNumberAccordingToPython == 5):
        return str("Saturday")
    elif(todaysNumberAccordingToPython == 6):
        return str("Sunday")


