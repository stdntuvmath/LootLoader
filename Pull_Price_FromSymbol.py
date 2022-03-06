from tda import  client
import datetime
import json


def GetPrice_EveryMinute(authentication, symbol):#authentication is required for this method


    currentYear = datetime.date.today().year
    currentMonth = datetime.date.today().month
    currentDay = datetime.date.today().day
    today = datetime.datetime(currentYear, currentMonth, currentDay)

    previousDay = datetime.datetime.now() - datetime.timedelta(1)
    previousDayYear = previousDay.year
    previousDayMonth = previousDay.month
    previousDayDay = previousDay.day
    yesterDay = datetime.datetime(previousDayYear, previousDayMonth, previousDayDay)



    price = authentication.get_price_history(symbol,
            period_type=client.Client.PriceHistory.PeriodType.DAY,
            period=client.Client.PriceHistory.Period.ONE_DAY,#this chooses one day ago, two days ago, ...etc.
            frequency_type=client.Client.PriceHistory.FrequencyType.MINUTE,
            frequency=client.Client.PriceHistory.Frequency.EVERY_MINUTE,
            start_datetime=yesterDay,
            end_datetime=today,
            need_extended_hours_data='true')
    assert price.status_code == 200, price.raise_for_status()

    
    priceJson = json.dumps(price.json(), indent=4)

    return priceJson