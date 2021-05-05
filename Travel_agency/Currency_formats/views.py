from rest_framework.decorators import api_view
from rest_framework.response import Response

from Currency_formats.models import Country
from .settings import fomat_settings
from .settings import status_code

from Currency_formats.api.serializers import CountrySerializer


@api_view(['GET'])
def get_countries(request):

    country = Country.objects.all() # Array list from objects
    country_serializer = CountrySerializer(country, many= True)
    
    return Response(country_serializer.data)
    


@api_view(['POST'])
def send_country(request):
    print(request.data)
    country_serializer = CountrySerializer(data = request.data)
    if country_serializer.is_valid():
        country_serializer.save()
        return Response(status_code.STATUS_CODE[200]) # Return status code and message
    else:
        return Response(status_code.STATUS_CODE[400])



@api_view(['PUT'])
def update_country(request,country):

    if country is not None:

        country_ = Country.objects.filter(country_name = country).first()
        country_serializer = CountrySerializer(country_, data = request.data)

        if country_serializer.is_valid():
            country_serializer.save()
            return Response(status_code.STATUS_CODE[200]) # Return status code and message
        else:
            return Response(status_code.STATUS_CODE[400])
        

@api_view(['DELETE'])
def delete_country(request,country):

    if country is not None:
        country_data = Country.objects.filter(country_name = country).first()
        country_serializer = CountrySerializer(country_data, data = {
            "country_name": country_data["country_name"],
            "country_status": "INACTIVE",
            "country_price": country_data["country_price"],
            "currency": [
                {
                    "currency_symbol": country_data["currency"][0]["currency_symbol"],
                    "currency_bool_symbol": country_data["currency"][0]["currency_bool_symbol"],
                    "currency_BA": country_data["currency"][0]["currency_BA"],
                    "currency_cents": country_data["currency"][0]["currency_cents"],
                    "currency_format": country_data["currency"][0]["currency_format"]
                }
            ],
            "_cls": "Country"
        })
        
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(status_code.STATUS_CODE[200])
        else:
            return Response(country_serializer.errors)
    else:
        return Response(status_code.STATUS_CODE[400])



@api_view(['GET'])
def selecte_one(request,country):

    country_selected = Country.objects.filter(country_name = country).first()
    country_selected_serializer = CountrySerializer(country_selected)
    print(country_selected_serializer.data["country_price"])
    return Response({"Country":country_selected_serializer.data["country_name"]
        ,"currency":fomat_settings.show_currency_by_info({

            "price":country_selected_serializer.data["country_price"],
            "bool_symbol":country_selected_serializer.data["currency"][0]["currency_bool_symbol"],
            "cents": country_selected_serializer.data["currency"][0]["currency_cents"],
            "format":  country_selected_serializer.data["currency"][0]["currency_format"],
            "symbol_ba": country_selected_serializer.data["currency"][0]["currency_BA"],
            "symbol":country_selected_serializer.data["currency"][0]["currency_symbol"]
        })})


