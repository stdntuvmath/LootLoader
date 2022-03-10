# IMPORTANT NOTE: YOU CANNOT ASK TDA SERVER FOR HISTORICAL DATA ON DAYS THAT THE MARKET IS NOT OPENED. IF YOU DO
# YOU GET error: Bad Request which is a 400 error even though the server is the one creating the issue.



from tda.client import Client
from tda.auth import client_from_token_file
from datetime import datetime, timedelta
import config_TDA_Live



client = client_from_token_file(config_TDA_Live.token_path, config_TDA_Live.api_key)

# client = easy_client(
#     api_key=config_TDA_Live.api_key,
#     redirect_uri=config_TDA_Live.redirect_url,
#     token_path=config_TDA_Live.token_path)



result = client.get_price_history('AMD',
                                frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                                need_extended_hours_data=True,
                                start_datetime=datetime.today() - timedelta(days=1),
                                end_datetime=datetime.now())

print(result)

pricedata = result.json()

print(pricedata)