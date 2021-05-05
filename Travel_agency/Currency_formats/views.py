from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.forms.models import model_to_dict

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action

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
            #return Response(country_serializer.data)
            return Response(status_code.STATUS_CODE[200]) # Return status code and message
        else:
            return Response(status_code.STATUS_CODE[400])
    except Exception as e:
        return Response(str(e))


@api_view(['PUT'])
def update_country(request,country):

    try:
        if country is not None:

            country_ = Country.objects.filter(country_name = country).first()
            country_serializer = CountrySerializer(country_, data = request.data)

            if country_serializer.is_valid():
                country_serializer.save()
                #return Response(country_serializer.data)
                return Response(status_code.STATUS_CODE[200]) # Return status code and message
            else:
                #return Response(country_serializer.errors)
                return Response(status_code.STATUS_CODE[400])
        
    except Exception as e:
        return Response({"error message": str(e)})

@api_view(['DELETE'])
def delete_country(request,country):
    """
    In this method there are two ways to perform the correct "DELETE" method:

        1   As the name suggests, delete the respective row, but, 
            in terms of auditing, deleting elements from the database 
            is not so feasible, 
            
        2   Created a new field "status",since when you want to delete a field , 
            just put it in inactive state but the information is not erased. 
            But, anyway I will put the method to delete the data
    """


    """

    1) First Method.  Uncomment and use
    try:
        
        if country is not None:

            country_data = Country.objects(country_name = country).first()
            country_data.delete()
            return Response(status_code.STATUS_CODE[200])

    except Exception as e:
        return Response({"error message": str(e)})


    """



    # 2) Second method. 
    try:
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
    except Exception as e:
        return Response({'error message':str(e)})
    


@api_view(['GET'])
def selecte_one(request,country):
    try:
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

    except Exception as e:
        return Response(str(e))


"""
Multiple inserts


[
    {
        "id": "60919727fb71db53cca36e00",
        "country_name": "United States",
        "country_price": 1750.5,
        "currency": [
            {
                "currency_symbol": "USD",
                "currency_bool_symbol": true,
                "currency_BA": true,
                "currency_cents": true,
                "currency_format": true
            }
        ],
        "_cls": "Country"
    },
    {
        "id": "60919e13a717611ee4c87360",
        "country_name": "Spain",
        "country_price": 675.5,
        "currency": [
            {
                "currency_symbol": "EUR",
                "currency_bool_symbol": true,
                "currency_BA": false,
                "currency_cents": false,
                "currency_format": true
            }
        ],
        "_cls": "Country"
    },
    {
        "id": "60919f4f2d9b8f582d6ac54d",
        "country_name": "Germany",
        "country_price": 1325.5,
        "currency": [
            {
                "currency_symbol": "EUR",
                "currency_bool_symbol": true,
                "currency_BA": true,
                "currency_cents": false,
                "currency_format": false
            }
        ],
        "_cls": "Country"
    },
    {
        "id": "6091d2c80023910b9c5801e7",
        "country_name": "Argentina",
        "country_price": 1250.5,
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
]




"""