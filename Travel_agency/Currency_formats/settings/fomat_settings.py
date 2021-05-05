
def show_currency_by_info(country_format:dict())->str:
    #currency_format = price
    currency_formatted = country_format['price'] # # This one is float
    currency_symbol = ""
    if country_format['bool_symbol']:
        currency_symbol = country_format['symbol']


    if (country_format['cents'] is False): # That's means, if is True, show me cents.
        currency_formatted = int(currency_formatted)
    elif (country_format['cents']) and country_format['format'] :
        currency_formatted = "${:,2f}".format(currency_formatted)
    elif  (country_format['cents']) and( country_format['format'] is False):
        currency_formatted = "${:.2f}".format(currency_formatted)
        


    if country_format['symbol_ba']:
        currency_formatted =  currency_symbol + " "+ str(currency_formatted)
    else:
        currency_formatted = str(currency_formatted) + " "+currency_symbol


    return currency_formatted

