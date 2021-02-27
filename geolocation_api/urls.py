from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('api01/auth/', include('rest_framework.urls')),
    path('api01/locate/<int:id>', views.LocatorDetailedView.as_view(),
         name='loc-rud'),
    path('api01/locate/', views.LocatorListView.as_view(),
         name='loc-list-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
