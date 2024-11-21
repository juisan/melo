# biblioteca/views.py
from rest_framework import generics
from .models import Colecao
from .serializers import ColecaoSerializer
from .permissions import IsColecionador  # Importação da permissão personalizada

class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionador]

    def perform_create(self, serializer):
        # Vincula o usuário autenticado à coleção criada
        serializer.save(colecionador=self.request.user)


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionador]