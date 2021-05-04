#from djongo import models

from mongoengine import *

class Currency(EmbeddedDocument):
    
    currency_symbol = StringField(required = True)
    currency_bool_symbol = BooleanField(null = True, default=True) # Option True means, currency symbol will be before price
    currency_BA = BooleanField(null = True, default=True) # Option True means, currency symbol will be before price
    currency_cents = BooleanField(null = True, default=True) # Option True means, show cents
    currency_format = BooleanField(null = True, default=True) # Option True means, format like this #,###,##
    #meta = {'allow_inheritance': True}



class Country(Document):

    country_name = StringField(required = True,max_length=50)
    country_price = FloatField()
    currency = ListField(EmbeddedDocumentField(Currency))
    meta = {'allow_inheritance': True}


