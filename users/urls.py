from django.urls import path
from users import views

# Create a router and register our viewsets with it.


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('create', views.CreateUserView.as_view(), name='user-create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-details'),
    path('<int:pk>/update', views.UpdateUserView.as_view(), name='user-update'),
]


