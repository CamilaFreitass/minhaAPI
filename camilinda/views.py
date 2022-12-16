from rest_framework import viewsets, generics
from camilinda.models import Atividade, Relatorio
from camilinda.serializer import AtividadeSerializer, RelatorioSerializer, ListaRelatorioAtividadeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AtividadesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    # queryset é um conjunto de ações que serão realizadas no banco de dados
    # ou seja, podemos criar, buscar, atualizar ou deletar os dados sem escrever a query SQL
    queryset = Atividade.objects.all()
    # quem vai ser a classe responsável por serializar essas atividades
    serializer_class = AtividadeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# é preciso verificar cada verbo do HTTP (GET, POST)? Não, apenas com essas linhas
# de código vamos conseguir manipular todas as requisições e informações que queremos disponibilizar

class RelatorioViewSet(viewsets.ModelViewSet):
    """Listando todos os relatórios"""
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

# nessa classe queremos apenas listar os recursos
class ListaRelatorioAtividade(generics.ListAPIView):
    """Listando o relatório de uma atividade"""
    def get_queryset(self):
        queryset = Relatorio.objects.filter(atividade_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaRelatorioAtividadeSerializer
