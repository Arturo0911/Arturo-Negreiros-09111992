from djongo import models



class Currency(models.Model):
    
    currency_symbol = models.BooleanField(default=True) # Option True means, currency symbol will be before price
    currency_AF = models.BooleanField(default=True) # Option True means, currency symbol will be before price
    currency_cents = models.BooleanField(default=True) # Option True means, show cents
    currency_format = models.BooleanField(default=True) # Option True means, format like this #,###,##

    class Meta:
        abstract = True

class Currency_(models.Model):

    currency = models.EmbeddedField(model_container = Currency)

    class Meta:
        abstract = True



class Country(models.Model):

    _id = models.ObjectIdField()
    country_name = models.CharField(max_length=50)
    country_price = models.FloatField()
    currency = models.EmbeddedField(model_container=Currency_)
    objects = models.DjongoManager()

    def __str__(self):
        return self.country_price


"""country = Country.objects.create(
    country_name="Germany",
    country_price=250,
    currency = {
        'currency_symbol': True,
        'currency_AF': True,
        'currency_cents': False,
        'currency_format': False,
    }
)"""