from django.db import models

class Atividade(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    SITUACAO = (
        ('F', 'Feita'),
        ('C', 'Cancelada'),
        ('P', 'Pendente')
    )
    # eu já tenho essa atividade criada em outra tabela,
    # eu apenas quero pegar o id dessa tabela e armazenar aqui no Relatorio
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    # o on_delete referencia que quando uma atividade for deletada, o relatório sobre essa atividade também será
    situacao = models.CharField(max_length=1, choices=SITUACAO, blank=False, null=False, default='P')