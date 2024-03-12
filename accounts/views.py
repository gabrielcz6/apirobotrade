from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer  # Asegúrate de importar el serializador


# Create your views here.
class LicenseExpiryDateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)
    



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser

class UpdateHddAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtén el usuario actual basado en el token de autenticación
        user = request.user
        # Obtén el nuevo valor para el campo 'hdd' de la solicitud
        new_hdd = request.data.get('hdd', None)
        if new_hdd is not None:
            # Actualiza el campo 'hdd' del usuario
            user.hdd = new_hdd
            user.save()
            return Response({"message": "Campo 'hdd' actualizado correctamente."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "El campo 'hdd' es requerido."}, status=status.HTTP_400_BAD_REQUEST)