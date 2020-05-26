"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from users import urls as users_urls
from friendships import urls as friendships_urls
from transactions import urls as transactions_urls
from .api import api_root, users_api_root, friends_api_root, transactions_api_root


def go_to_api(request):
    return redirect('api/')


urlpatterns = [
    path('', go_to_api),
    path('api/', api_root, name='api-root'),
    path(users_urls.users_root_url, users_api_root, name='users-api'),
    path(friendships_urls.friends_root_url, friends_api_root, name='friends-api'),
    path(transactions_urls.transactions_root_url, transactions_api_root, name='transcations-api'),
]


urlpatterns += users_urls.urlpatterns
urlpatterns += friendships_urls.urlpatterns
urlpatterns += transactions_urls.urlpatterns


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


