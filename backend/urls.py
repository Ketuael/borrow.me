"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users import urls as users_urls
from friendships import urls as friendships_urls
from transactions import urls as transactions_urls


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users API': reverse('users-api', request=request, format=format),
        'Friends API': reverse('friends-api', request=request, format=format),
        'Transcations API': reverse('transcations-api', request=request, format=format),
    })


def go_to_api(request):
    return redirect('api/')


urlpatterns = [
    path('', go_to_api),
    path('api/', api_root, name='api-root'),
    path('api/users', include(users_urls), name='users-api'),
    path('api/friends', include(friendships_urls), name='friends-api'),
    path('api/transactions', include(transactions_urls), name='transcations-api'),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


