
"""
function to generated the right presentation
"""



def show_currency_by_info(country_format:dict()):
    #currency_format = price
    currency_formatted = 250.0#(country_format['price']) # # This one is float
    currency_symbol = ""
    if country_format['bool_symbol']:
        currency_symbol = country_format['symbol']


    if country_format['cents']: # That's means, if is True, show me cents.
        currency_formatted = int(currency_formatted)


    if country_format['format']:
        currency_formatted = "${:,2f}".format(currency_formatted)
    else:
        currency_formatted = "${:.2f}".format(currency_formatted)


    if country_format['symbol_ba']:
        currency_formatted =  currency_symbol + " "+ str(currency_formatted)
    else:
        currency_formatted = str(currency_formatted) + " "+currency_symbol


    return currency_formatted



def wherever(dictionary:dict()) ->str:
    
    print(str(dictionary['greet']))

    for x in dictionary:
        print(dictionary[x])

    return "hi"
