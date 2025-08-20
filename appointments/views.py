from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppointmentSerializer
from drf_yasg.utils import swagger_auto_schema


class AppointmentCreateView(APIView):
    @swagger_auto_schema(request_body=AppointmentSerializer)
    def post(self, request):
        # print("Incoming data:", request.data)
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()
            return Response(AppointmentSerializer(appointment).data, status=status.HTTP_201_CREATED)
        # print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
