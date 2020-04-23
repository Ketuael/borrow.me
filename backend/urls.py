"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""

#from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
import users.urls


def go_to_api(request):
    return redirect('api/')


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', go_to_api),
    path('api/', include(users.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
