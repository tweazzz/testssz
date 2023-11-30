from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Prepod, JobHistory
from .serializers import PrepodSerializer, JobHistorySerializer, PrepodCreateSerializer

class PrepodViewSet(viewsets.ModelViewSet):
    queryset = Prepod.objects.all()
    serializer_class = PrepodSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return PrepodCreateSerializer
        return PrepodSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PrepodCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PrepodCreateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobHistoryViewSet(viewsets.ModelViewSet):
    queryset = JobHistory.objects.all()
    serializer_class = JobHistorySerializer