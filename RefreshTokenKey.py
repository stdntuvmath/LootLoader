import tdameritrade.auth
import Documentation.config_TDA_Live as config_TDA_Live

answer = tdameritrade.auth.authentication(config_TDA_Live.client_id, config_TDA_Live.redirect_url)

print(answer)

#Step 1: Run this code
#Step 2: Put in credentials for Ameritrade (TOS creds)
#Step 3: get code from ginas phone and input it into TDA's web app
#Step 4: see the screen that says 404 failure
#Step 5: go back to the code and click into the Terminal below
#Step 6: press enter
#Step 7: Copy the new access and refresh codes into and over the old codes stored in token.json
#Step 8: save token.json changes