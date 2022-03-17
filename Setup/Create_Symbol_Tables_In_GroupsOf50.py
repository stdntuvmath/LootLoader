import pyodbc
import regex as re


def CreateTables():
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM Symbols')

    symbolList = [] #you have to start with a list and then convert it to a tuple

    counter = 0

    for i in cursor:
        if(counter < 51):
            break
        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)
        counter+=1
    counter=0
    
    for symbol in symbolList:
        if(counter < 51):
            cursor.execute('IF NOT EXISTS(SELECT * FROM sysobjects WHERE name=\'{}\')\n'+
            'CREATE TABLE LootLoader.dbo.{} (Symbol nchar(4), Price float, nDate date, nTime time(0))'.format(symbol,symbol))
            cursor.commit()
        counter = counter+1
    cursor.close()