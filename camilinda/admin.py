from django.contrib import admin
from camilinda.models import Atividade, Relatorio

class Atividades(admin.ModelAdmin):
    # o list_display controla quais campos são mostrados na listagem do admin.
    # obs: o 'id' é gerado sempre que criamos um modelo
    list_display = ('id', 'nome', 'descricao', 'data')
    # list_display_links indica em quais campos vai ser possível clicar para fazer alteração
    list_display_links = ('id', 'nome')
    # search_field é o campo de busca e o argumento é a indicação de por qual característica vai ser feita a busca
    search_fields = ('nome',)
    # list_per_page indica quantas atividades vão ter por página
    list_per_page = 20

admin.site.register(Atividade, Atividades)

class Relatorios(admin.ModelAdmin):
    list_display = ('id', 'atividade', 'situacao')
    list_display_links = ('id', 'atividade')

admin.site.register(Relatorio, Relatorios)