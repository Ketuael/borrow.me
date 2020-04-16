from rest_framework import generics
from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
from rest_framework import permissions
from users.permissions import IsSelf

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

    permission_classes = [IsSelf]


