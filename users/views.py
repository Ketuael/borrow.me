from rest_framework import generics
from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
<<<<<<< HEAD
from rest_framework import permissions
from users.permissions import IsSelf
=======
from rest_framework import filters
from users.permissions import IsSelf, IsFriend
>>>>>>> develop

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
<<<<<<< HEAD
=======
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']
>>>>>>> develop


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

<<<<<<< HEAD
=======
    #permission_classes = [IsSelf | IsFriend]

>>>>>>> develop

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

    permission_classes = [IsSelf]


