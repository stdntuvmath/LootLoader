import Documentation.config_TDA_Live as config_TDA_Live
from tda import auth


def Authenticate():
    try:
        c = auth.client_from_token_file(config_TDA_Live.token_path, config_TDA_Live.api_key)
        return c
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome() as driver:
            c = auth.client_from_login_flow(#I think this prompts the user with TDA login screen
                driver, config_TDA_Live.api_key, config_TDA_Live.redirect_uri, config_TDA_Live.token_path)

            