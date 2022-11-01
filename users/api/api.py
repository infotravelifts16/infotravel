
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.api.serializers import UserSerializer, UserListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from users.models import User


@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':

        user = User.objects.all().values('id','username','email', 'password')
        users_serializer = UserListSerializer(user, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario creado correctamente'}, status = status.HTTP_201_CREATED)


        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

    user = User.objects.filter(id = pk).first()


    if user:

        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)


        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data= request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
        
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)



        elif request.method == 'DELETE':
            user.delete()
            Response({'message': 'Usuario eliminado correctamente'}, status = status.HTTP_200_OK)


    Response({'message': 'Usuario no encontrado'}, status = status.HTTP_400_BAD_REQUEST)