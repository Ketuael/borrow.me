from rest_framework import generics
from rest_framework import views
from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer, CreateUserSerializer, UpdateUserSerializer
from rest_framework import filters
from users.permissions import IsSelf, IsFriend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class HelloView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    #permission_classes = [IsSelf | IsFriend]


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

    permission_classes = [IsSelf]


