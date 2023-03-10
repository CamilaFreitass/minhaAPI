# Generated by Django 4.1.4 on 2022-12-13 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camilinda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('F', 'Feita'), ('C', 'Cancelada'), ('P', 'Pendente')], default='P', max_length=1)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camilinda.atividade')),
            ],
        ),
    ]
