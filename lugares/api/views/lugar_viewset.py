from rest_framework import generics, status, viewsets
from base.api import GeneralListApiView

from lugares.api.serializers.lugar_serializers import LugarSerializer

from users.api.authentication_mixins import Authentication
from rest_framework.response import Response


class LugarViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = LugarSerializer

    def get_queryset(self, pk = None ):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def list(self, request):
        lugar_serializer =  self.get_serializer(self.get_queryset(),many = True)
        return Response(lugar_serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        serializer =  self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'Lugar creado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        if self.get_queryset(pk):
            lugar_serializer =  self.serializer_class(self.get_queryset(pk), data = request.data)
            if lugar_serializer.is_valid():
                lugar_serializer.save()
                return Response(lugar_serializer.data, status = status.HTTP_200_OK )
            return Response(lugar_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        lugar = self.get_queryset().filter(id = pk).first()
        if lugar:
            lugar.state = False
            lugar.save()
            return Response({'message': 'Lugar eliminado correctametne'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un Lugar con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
    




