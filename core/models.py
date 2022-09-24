from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=500, default='Nome pessoa')
    cpf_pessoa = models.CharField(max_length=500, default='000.000.000-00')
    descricao_pessoa = models.CharField(max_length=500, default='Breve descricao para o site')
    cargo = models.CharField(max_length=50, default='Cargo')
    email_pessoa = models.EmailField('email', max_length=50)
    #img-pessoa = Aqui fica uma imagem para a pessoa

    def __str__(self):
        return self.nome_pessoa


class Produto(models.Model):
    descricao_produto = models.CharField(max_length=200, default='Breve descricao produto')
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField('quantidade em estoque')
#   img-produto = imagem para o produto
    def __str__(self):
        return self.descricao_produto


class Servicos(models.Model):
    nome_servico = models.CharField(max_length=15)
    descricao_servicos = models.CharField(max_length=200)
    #img-servico = imagem para servico

    def __str__(self):
        return self.nome_servico


class Blog(models.Model):
    title_post = models.CharField(max_length=100, default='Título')
    resume_post = models.CharField(max_length=100, default='resumo')
    text_post = RichTextUploadingField(default='Texto')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    #Aqui deve ter uma variavel de imagem para o post

    def __str__(self):
        return self.title_noticia
