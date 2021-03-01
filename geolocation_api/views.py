import os, requests

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Locator
from .serializers import LocatorSerializer
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
# from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

# Create your views here.


# @api_view(['GET'])
# def default(request):
#     # return HttpResponse('default api view')
#     return redirect('loc-list-create')


@csrf_exempt
def default_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    base_url = f'http://api.ipstack.com/check?access_key=' \
               f'{os.getenv("ipstackKey")}'

    if request.method == 'GET':
        locations = Locator.objects.all()
        serializer = LocatorSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        ip_data_dict = requests.get(base_url).json()
        # r = requests.post('https://httpbin.org/post', data=ip_data_dict)
        data = JSONParser().parse(request)
        serializer = LocatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class LocatorListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = LocatorSerializer
    queryset = Locator.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LocatorDetailedView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = LocatorSerializer
    queryset = Locator.objects.all()
