from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView


from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action

from Currency_formats.models import Country
from Currency_formats.settings import fomat_settings

from Currency_formats.api.serializers import CountrySerializer

#class Country_currency(APIView):

@api_view(['GET'])
def get_countries(request):

    country = Country.objects.all() # Array list from objects
    country_serializer = CountrySerializer(country, many= True)
    
    return Response(country_serializer.data)
    


@api_view(['POST'])
def send_country(request):

    """
        {
        "country_name": "Argentina",
        "country_price": 1250.50,
        "currency": [
            {
                "currency_symbol": "USD",
                "currency_bool_symbol": true,
                "currency_BA": true,
                "currency_cents": false,
                "currency_format": true
            }
        ],
        "_cls": "Country"
        }
    """
    try:
        print(request.data)
        country_serializer = CountrySerializer(data = request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(country_serializer.data)

    except Exception as e:
        return Response(str(e))


@api_view(['PUT'])
def update_country(request,country):
    return Response({'message':"PUT METHOD"})


@api_view(['DELETE'])
def delete_country(request,country):
    return Response({'message':"DELETE METHOD"})


@api_view(['GET'])
def selecte_one(request,country):
    try:
        country_selected = Country.objects.filter(country_name = country).first()
        country_selected_serializer = CountrySerializer(country_selected)
        #print(country_selected_serializer.data)


        for i in country_selected_serializer.data["currency"]:
            for j in i:
                print(j, i[j])
    
        return Response(country_selected_serializer.data)

    except Exception as e:
        return Response(str(e))


"""
# READ ALL 
def index(request):
    
    if request.method == 'GET':
        return HttpResponse("GET METHOD")
    # Generating the fields
    germany_format = Currency(currency_symbol = "EUR",currency_bool_symbol= True ,currency_BA = True,
        currency_cents = False,currency_format= False )
    germany_country = Country(country_name = "Germany", country_price= 250)
    germany_country.currency.append(germany_format)
    germany_country.save()
    return HttpResponse("<h1>Working!</h1>")


def insert_data(request):

    if request.method == 'POST':
        print(request.body)
        return HttpResponse(body)
"""


"""
# READ BY ONE
def find_country(request, country):

    # store data
    try:
        country = Country.objects(country_name = country).first()   
        return HttpResponse(fomat_settings.show_currency_by_info({
            "price":country.country_price,
            "bool_symbol":country.currency[0].currency_bool_symbol,
            "cents": country.currency[0].currency_cents,
            "format":  country.currency[0].currency_format,
            "symbol_ba": country.currency[0].currency_BA,
            "symbol": country.currency[0].currency_symbol
        }))
                
    except Exception as e:
        return HttpResponse(str(e))

# UPDATE
def update_country_info(request):
    pass




# DELETE
def delete_country_info(request):
    pass

"""





