from msilib.schema import Error
import pyodbc
import regex as re
from time import sleep


def Create_Individual_Symbol_Tables_InLootLoader_DB():
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM Symbols')

    symbolList = [] #you have to start with a list and then convert the list to a tuple

    for i in cursor:

        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)  

    for symbol in symbolList:
    
        cursor.execute('CREATE TABLE {} (Symbol nchar, Price float, nTime datetime)'.format(symbol))
        cursor.commit()
        sleep(0.2)

 