import pyodbc
import regex as re


def ClearTables():
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

        cursor.execute('DELETE {}'.format(symbol))
        cursor.commit()

        cursor.execute('DELETE {}_EMA200'.format(symbol))
        cursor.commit()

    cursor.close()