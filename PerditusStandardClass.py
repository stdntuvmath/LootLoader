class ConvertToProtobufFormat:


    def convertTDAmeritradeHistoricalToProtobufFormat(pythonObject):
        pythonObject["timestamp"] = pythonObject.pop("datetime")


    def convertTDApiLiveDataToProtobufFormat(pythonObject):
        pythonObject["symbol"] = pythonObject.pop("key")
        pythonObject["open"] = pythonObject.pop("OPEN_PRICE")
        pythonObject["close"] = pythonObject.pop("CLOSE_PRICE")
        pythonObject["low"] = pythonObject.pop("LOW_PRICE")
        pythonObject["high"] = pythonObject.pop("HIGH_PRICE")
        pythonObject["volume"] = pythonObject.pop("VOLUME")
        pythonObject["timestamp"] = pythonObject.pop("CHART_TIME")


    def convertPolygonHistoricalDataFormatToProtobufFormat(pythonObject):
        pythonObject["open"] = pythonObject.pop("o")
        pythonObject["close"] = pythonObject.pop("c")
        pythonObject["low"] = pythonObject.pop("l")
        pythonObject["high"] = pythonObject.pop("h")
        pythonObject["volume"] = pythonObject.pop("v")
        pythonObject["timestamp"] = pythonObject.pop("t")

    