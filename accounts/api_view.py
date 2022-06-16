from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework import status
from accounts.serializers import RegisterSerializers, UserDetailSerializers, UserRegistrSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers


class UserDetailView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializers

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


