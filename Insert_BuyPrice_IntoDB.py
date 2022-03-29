import pyodbc


def InsertBuyPrice(symbol, buyPrice, numberOfShares):#returns a float number

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('INSERT INTO {}_BuyPrice VALUES (\'{}\', \'{}\')'.format(symbol, buyPrice, numberOfShares))
    
    cursor.commit()
    cursor.close()