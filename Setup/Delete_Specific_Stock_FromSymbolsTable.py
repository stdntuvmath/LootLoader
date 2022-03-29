import pyodbc


def Delete_Symbol_AND_Tables(symbol):
    

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM Symbols')

    
    
    #delete tables

    cursor.execute('DROP TABLE {}_Historical'.format(symbol))
    cursor.commit()

    cursor.execute('DROP TABLE {}_BuyPrice'.format(symbol))
    cursor.commit()
    
    #delete stock from symbol list

    cursor.execute('DELETE FROM LootLoader.dbo.Symbols WHERE Symbol=\'{}\''.format(symbol))
    cursor.commit()

    cursor.close()