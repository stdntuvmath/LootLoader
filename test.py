import Get_Newest_Historical_Data
import All_Symbols

allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()

for symbol in allSymbols:
    oldRecord = Get_Newest_Historical_Data.Pull_LastLine_of_HistoricalData_FromDB(symbol)

    print(oldRecord[0])
    print(len(oldRecord))

    