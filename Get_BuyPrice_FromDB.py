import pyodbc


def GetBuyPrice(symbol):#returns a float number

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT * FROM {}_BuyPrice'.format(symbol))

    array=[]

    for i in cursor:

        array.append(i)
        

    buyPrice = array[0]
    cursor.close()
    
    return buyPrice







def Get_numberOfShares(symbol):#returns a float number

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT * FROM {}_BuyPrice'.format(symbol))

    array=[]

    for i in cursor:

        array.append(i)
        

    numberOfShares = array[1]
    cursor.close()
    
    return numberOfShares
    