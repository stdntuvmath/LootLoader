
#https://tda-api.readthedocs.io/en/latest/streaming.html

from asyncio.windows_events import NULL
from logging import exception
from symtable import Symbol
from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient
from os.path import exists
from ta import trend


import json
import config_TDA_Live
import OAuth_Authenticate
import matplotlib.pyplot as plt
import numpy as np
import pytz
import datetime
import asyncio
import Stream_Price_


nasdaqSymbols = NASDAQ_Symbols.Return_NASDAQ_Symbols_FromDB()
nyseSymbols = NYSE_Symbols.Return_NYSE_Symbols_FromDB()

#print(nasdaqSymbols)

client = OAuth_Authenticate.Authenticate()

stream_client = StreamClient(client, account_id=config_TDA_Live.account_id)

async def read_stream():


    symbolTuple = ("A", "AAL", "AAP", "AAPL", "ABBV", "ABC", "ABMD", "ABT", "ACN",
						 "ADBE", "ADI", "ADM", "ADP", "ADS", "ADSK", "AEE", "AEP", "AES", "AFL",
						 "AIG", "AIV", "AIZ", "AJG", "AKAM", "ALB", "ALGN", "ALK", "ALL",
						 "ALLE", "AMAT", "AMCR", "AMD", "AME", "AMGN", "AMP", "AMT", "AMZN",
						 "ANET", "ANSS", "ANTM", "AON", "AOS", "APA", "APD", "APH", "APTV", "ARE",
						 "ARNC", "ATO", "ATVI", "AVB", "AVGO", "AVY", "AWK", "AXP", "AZO", "BA",
						 "BAC", "BAX", "BBY", "BDX", "BEN", "BF.B", "BIIB", "BK", "BKNG", "BKR",
						 "BLK", "BLL", "BMY", "BR", "BRK.B", "BSX", "BWA", "BXP", "C", "CAG", "CAH",
						 "CAT", "CB", "CBRE", "CCI", "CCL", "CDNS", "CDW", "CE", "CERN", "CF", "CFG",
						 "CHD", "CHRW", "CHTR", "CI", "CINF", "CL", "CLX", "CMA", "CMCSA", "CME",
						 "CMG", "CMI", "CMS", "CNC", "CNP", "COF", "COO", "COP", "COST", "COTY",
						 "CPB", "CPRI", "CPRT", "CRM", "CSCO", "CSX", "CTAS", "CTL", "CTSH", "CTVA",
						 "CTXS", "CVS", "CVX", "CXO", "D", "DAL", "DD", "DE", "DFS", "DG", "DGX", 
						 "DHI", "DHR", "DIS", "DISCA", "DISCK", "DISH", "DLR", "DLTR", "DOV", "DOW",
						 "DRE", "DRI", "DTE", "DUK", "DVA", "DVN", "DXC", "EA", "EBAY", "ECL", "ED",
						 "EFX", "EIX", "EL", "EMN", "EMR", "EOG", "EQIX", "EQR", "ES", "ESS",
						 "ETN", "ETR", "EVRG", "EW", "EXC", "EXPD", "EXPE", "EXR", "F", "FANG", "FAST",
						 "FB", "FBHS", "FCX", "FDX", "FE", "FFIV", "FIS", "FISV", "FITB",
						 "FLS", "FLT", "FMC", "FOX", "FOXA", "FRC", "FRT", "FTI", "FTNT", "FTV", "GD",
						 "GE", "GILD", "GIS", "GL", "GLW", "GM", "GOOG", "GOOGL", "GPC", "GPN", "GPS",
						 "GRMN", "GS", "GWW", "HAL", "HAS", "HBAN", "HBI", "HCA", "HD", "HES", "HFC",
						 "HIG", "HII", "HLT", "HOG", "HOLX", "HON", "HP", "HPE", "HPQ", "HRB", "HRL",
						 "HSIC", "HST", "HSY", "HUM", "IBM", "ICE", "IDXX", "IEX", "IFF", "ILMN",
						 "INCY", "INFO", "INTC", "INTU", "IP", "IPG", "IPGP", "IQV", "IR", "IRM",
						 "ISRG", "IT", "ITW", "IVZ", "J", "JBHT", "JCI", "JKHY", "JNJ", "JNPR", "JPM",
						 "JWN", "K", "KEY", "KEYS", "KHC", "KIM", "KLAC", "KMB", "KMI", "KMX", "KO",
						 "KR", "KSS", "KSU", "L", "LDOS", "LEG", "LEN", "LH", "LHX", "LIN", "LKQ",
						 "LLY", "LMT", "LNC", "LNT", "LOW", "LRCX", "LUV", "LVS", "LW", "LYB", "LYV",
						 "M", "MA", "MAA", "MAR", "MAS", "MCD", "MCHP", "MCK", "MCO", "MDLZ", "MDT",
						 "MET", "MGM", "MHK", "MKC", "MKTX", "MLM", "MMC", "MMM", "MNST", "MO", "MOS",
						 "MPC", "MRK", "MRO", "MS", "MSCI", "MSFT", "MSI", "MTB", "MTD", "MU", 
						 "NCLH", "NDAQ", "NEE", "NEM", "NFLX", "NI", "NKE", "NLOK", "NLSN",
						 "NOC", "NOV", "NOW", "NRG", "NSC", "NTAP", "NTRS", "NUE", "NVDA", "NVR", "NWL",
						 "NWS", "NWSA", "O", "ODFL", "OKE", "OMC", "ORCL", "ORLY", "OXY", "PAYC", "PAYX",
						 "PAYX", "PBCT", "PCAR", "PEAK", "PEG", "PEP", "PFE", "PFG", "PG", "PGR", "PH", 
						 "PHM", "PKG", "PKI", "PLD", "PM", "PNC", "PNR", "PNW", "PPG", "PPL", "PRGO", 
						 "PRU", "PSA", "PSX", "PVH", "PWR", "PXD", "PYPL", "QCOM", "QRVO", "RCL", "RE", 
						 "REG", "REGN", "RF", "RHI", "RJF", "RL", "RMD", "ROK", "ROL", "ROP", "ROST",
						 "RSG", "SBAC", "SBUX", "SCHW", "SEE", "SHW", "SIVB", "SJM", "SLB", "SLG",
						 "SNA", "SNPS", "SO", "SPG", "SPGI", "SRE", "STE", "STT", "STX", "STZ", "SWK", 
						 "SWKS", "SYF", "SYK", "SYY", "T", "TAP", "TDG", "TEL", "TFC", "TFX", "TGT",
						 "TJX", "TMO", "TMUS", "TPR", "TROW", "TRV", "TSCO", "TSN", "TT", "TTWO", "TWTR",
						 "TXN", "TXT", "UA", "UAA", "UAL", "UDR", "UHS", "ULTA", "UNH", "UNM", "UNP", "UPS",
						 "URI", "USB", "V", "VFC", "VIAC", "VLO", "VMC", "VNO", "VRSK", "VRSN",
						 "VRTX", "VTR", "VZ", "WAB", "WAT", "WBA", "WDC", "WEC", "WELL", "WFC", "WHR", 
						 "WLTW", "WM", "WMB", "WMT", "WRB", "WRK", "WU", "WY", "WYNN", "XEL", "XLNX", "XOM",
						 "XRAY", "XRX", "XYL", "YUM", "ZBH", "ZBRA", "ZION", "ZTS")


    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)#fastest available 500ms = EXPRESS, FAST=1second
    
    # Always add handlers before subscribing because many streams start sending
    # data immediately after success, and messages with no handlers are dropped.
    try:        

        #stream_client.add_chart_equity_handler(lambda msg: createFile(msg))       
        stream_client.add_chart_equity_handler(lambda msg: prepAndSendLiveData(msg))       


        await stream_client.chart_equity_subs(nyseSymbols[:20])#sends subscription request to the server

    except(exception):
        print(exception)  


    while True:
        await stream_client.handle_message()

def prepAndSendLiveData(data):
    
    priceArray = []
    timeArray = []
    symbolArray = []
    
    for candle in data["content"]:
        
        stockSymbol = candle.pop("key")

        closePrice = candle.pop("CLOSE_PRICE")

        epochTime = candle.pop("CHART_TIME")
    
        tz = pytz.timezone('US/Central')

        localTime = datetime.datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M')#from utc to local time

        # priceArray.append(closePrice)
        # timeArray.append(localTime)
        # symbolArray.append(stockSymbol)

        closePriceString = "{}, {}, {}\n".format(stockSymbol, closePrice, localTime)
        print(closePriceString)

        # file_exists = exists("PriceData\\Symbols_SP300_priceData.csv")    

        # if(file_exists == True):

        #     outFile = open("PriceData\\Symbols_SP300_priceData.csv", "a")
        #     outFile.write("{}".format(closePriceString))
        #     outFile.close()         

        # else:
        #     outFile = open("PriceData\\Symbols_SP300_priceData.csv", "a")
        #     outFile.write("{}".format(closePriceString))
        #     outFile.close()

async def retrieveLiveData(self):
    await self.m_streamClient.login()
    #Does the handler get all the different stocks all at once?
    #add_listed_book_handler is the NYSE
    self.m_streamClient.add_chart_equity_handler(lambda message: self.prepAndSendLiveData(message)) #this can be swapped with a function...
    #listed_book_subs is the NYSE
    await self.m_streamClient.chart_equity_subs(self.m_symbolsSP500[:300]) #300 is the max... Workaround to call other 200 via get stock history

    while True:
        await self.m_streamClient.handle_message()




def createFile(msg):

    jsonString = json.dumps(msg, indent=4)

    dictionary = json.loads(jsonString) #creates json dictionary object from jsonString

    priceArray = []
    timeArray = []
    symbolArray = []
    #trend.ema_indicator()

    #gets the close prices and times from the json dictionary object
    for key, value in dictionary.items():
        for i in (range(1)):
            closePrice = dictionary["content"][i]["CLOSE_PRICE"]
            epochTime = dictionary["content"][i]["CHART_TIME"]

            tz = pytz.timezone('US/Central')

            localTime = datetime.datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M')#from utc to local time

            priceArray.append(closePrice)
            timeArray.append(localTime)

            closePriceString = "{},{}\n".format(priceArray[-1], timeArray[-1])
            print(closePriceString)

    #         # y2 = dictionary["content"][i]["CLOSE_PRICE"]
    #         # x2 = dictionary["content"][i]["CHART_TIME"] 
    #         #closePriceString = "{},{},\n".format(closePrice, chartTime)
    # yPoints = np.array([priceArray[-1], priceArray[-2]])
    # xPoints = np.array([timeArray[-1], timeArray[-2]])
    # plt.plot(xPoints,yPoints)
    # plt.show()




            # file_exists = exists("PriceData\\{}_priceData.csv".format(symbolList))    

            # if(file_exists == True):

            #     outFile = open("PriceData\\{}_priceData.csv".format(symbolList), "a")
            #     outFile.write("{}".format(closePriceString))
            #     outFile.close()

                

            # else:
            #     outFile = open("PriceData\\{}_priceData.csv".format(symbolList), "a")
            #     outFile.write("{}".format(closePriceString))
            #     outFile.close()


          





  

 