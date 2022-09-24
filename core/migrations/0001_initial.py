# Generated by Django 4.1 on 2022-08-18 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=500)),
                ('cpf_pessoa', models.CharField(max_length=500)),
                ('cargo', models.CharField(max_length=50)),
                ('email_pessoa', models.EmailField(max_length=50, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_produto', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=6, max_digits=6)),
                ('estoque', models.IntegerField(verbose_name='quantidade em estoque')),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_servico', models.CharField(max_length=15)),
                ('descricao_servicos', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_noticia', models.CharField(default='aqui no titulo ta vazio', max_length=100)),
                ('resume_noticia', models.CharField(default='aqui no resumo ta vazio', max_length=200)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.pessoa')),
            ],
        ),
    ]
