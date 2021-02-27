from django.shortcuts import render, HttpResponse, redirect
from .models import Locator
from .serializers import LocatorSerializer
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
# from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

# Create your views here.


@api_view(['GET'])
def default(request):
    # return HttpResponse('default api view')
    return redirect('loc-list-create')


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
