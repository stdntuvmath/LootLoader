import pyodbc


def Insert_Symbol_Price_andDateTime_Data(symbol, price, date, time):
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()


    #insert data int table
    cursor.execute('INSERT INTO {} (Symbol, Price, nDate, nTime) VALUES (\'{}\', {}, \'{}\', \'{}\')'.format(symbol, symbol, price, date, time))
    cursor.commit()
    cursor.close()




def Insert_Symbol_EMA200_andDateTime_Data(symbol, price, date, time):
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()


    #insert data int table
    cursor.execute('INSERT INTO {}_EMA200 (Symbol, EMA200, nDate, nTime) VALUES (\'{}\', {}, \'{}\', \'{}\')'.format(symbol, symbol, price, date, time))
    cursor.commit()
    cursor.close()


