from tkinter import *
from logging import exception
import os
from time import sleep
from tkinter.ttk import PanedWindow
from typing_extensions import Self
from matplotlib.widgets import Widget
from tda import auth, client, orders
import json
import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna
from ta.trend import ema_indicator
import tda
import OAuth_Authenticate
import Pull_Symbols_FromTDA
import Pull_Symbols_FromTOScsv
import ta
import asyncio
import threading
import RetrieveLiveData
import All_Symbols
import Get_Historical_PriceData
import Setup.Create_Symbol_Tables as createTables
import Setup.Create_Symbol_Tables_EMA200 as createTablesEMA200
import Delete_Table_Data
import Setup.Delete_Symbol_Tables_FromDB as deleteTables
import TurnerBands
import Realtime_Data
import datetime
import Todays_Weekday
import time
import pytz



#first get and store necessary historical data to produce accurate real time data. 


#while within business hours, get realtime data
todaysDate = datetime.date.today()
startTime = datetime.datetime.strptime(str(todaysDate)+" 08:30:15",'%Y-%m-%d %H:%M:%S')
endTime = datetime.datetime.strptime(str(todaysDate)+" 14:59:00",'%Y-%m-%d %H:%M:%S')
now = datetime.datetime.now()
today = Todays_Weekday.Get_Todays_Weekday_Name()

if(startTime <= now and now < endTime and today !="Saturday" and today != "Sunday"):

    while startTime <= now and now < endTime and today !="Saturday" and today != "Sunday":
        
        now = datetime.datetime.now()
        print(now)
        Realtime_Data.Get_Price_Data(10)
        sleep(5)

    print("\n\n\nEnd Of Market Day.\n\n\nLootLoader powering down...")
else:
    #
    window = Tk()
    window.geometry("300x200+500+150")#position of screen
    window.title("Stock Market is Closed")
    

    screenLable = Label(text="The stock market is closed at the moment. Please try LootLoader again during market hours: 8:30AM-3:00PM, Monday through Friday.", fg="black",width=50, height=50, wraplength=225)
    screenLable.pack(fill= BOTH, expand= True, padx= 20, pady=20)
    window.mainloop()
    

#TurnerBands.Run_TurnerBands()

