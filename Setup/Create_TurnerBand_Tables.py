import pyodbc
import regex as re


def Create_TurnerBand_Historical_Tables():
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM Symbols')

    symbolList = [] #you have to start with a list and then convert it to a tuple

    for i in cursor:

        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)
    
    
    #delete tables
    for symbol in symbolList:

        cursor.execute('CREATE TABLE LootLoader.dbo.{}_Historical(Symbol nchar(4), nDate date, nTime time(0), Price float, EMA200 float, EMA200Angle float, stdrdDev1 float, stdrdDev2 float, stdrdDev3 float, stdrdDev4 float, stdrdDev5 float, stdrdDev6 float, stdrdDev7 float, stdrdDev8 float, stdrdDev9 float, stdrdDev10 float);'.format(symbol))
        cursor.commit()


    cursor.close()








def Create_TurnerBand_BuyPrice_Tables():
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM Symbols')

    symbolList = [] #you have to start with a list and then convert it to a tuple

    for i in cursor:

        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)
    
    
    #delete tables
    for symbol in symbolList:


        cursor.execute('CREATE TABLE LootLoader.dbo.{}_BuyPrice(Price float, numberOfShares int);'.format(symbol))
        cursor.commit()

    cursor.close()










def Create_TurnerBand_Account_Tables():
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM Symbols')

    symbolList = [] #you have to start with a list and then convert it to a tuple

    for i in cursor:

        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)
    
    
    #delete tables
    for symbol in symbolList:


        cursor.execute('CREATE TABLE LootLoader.dbo.Account_Test(accountValue float);')
        

    cursor.close()