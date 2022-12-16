from rest_framework import serializers
from camilinda.models import Atividade, Relatorio

# essa classe é para dizer qual modelo estamos utilizando
# e quais campos eu quero utilizar em cada serializer
class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'nome', 'descricao', 'data']

# o serializer vai funcionar como um filtro dos dados que queremos disponibilizar para a API
# ali em fields eu posso colocar todos os dados ou apenas aqueles que quero disponibilizar

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        exclude = []

class ListaRelatorioAtividadeSerializer(serializers.ModelSerializer):
    #no relatorio tem o 'id' da atividade, então aqui estou dizendo que a 'atividade' vai ser do tipo de leitura
    #e eu quero representar ela através do nome dela
    atividade = serializers.ReadOnlyField(source='atividade.nome')
    situacao = serializers.SerializerMethodField()
    class Meta:
        model = Relatorio
        fields = ['atividade', 'situacao']
    def get_situacao(self, obj):
        return obj.get_situacao_display()