from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import RPS
from .serializers import RPSSerializer


class RPSList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = RPS.objects.all()
    serializer_class = RPSSerializer

    def get_queryset(self):
        return RPS.objects.filter(prestador=self.request.user)

    def perform_create(self, serializer):
        serializer.save(prestador=self.request.user)


class RPSDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RPSSerializer

    def get_queryset(self):
        return RPS.objects.filter(prestador=self.request.user)