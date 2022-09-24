from django.shortcuts import render


def index(request):

    return render(request, 'indexteste.html')


def quemsomos(request):
    return render(request, 'quemsomos.html')


def servicos(request):
    return render(request, 'Servicos.html')


def produtos(request):
    return render(request, 'Produtos.html')


def portfolio(request):
    return render(request, 'Portfolio.html')


def faleconosco(request):
    return render(request, 'formcontato.html')


def equipe(request):
    return render(request, 'equipe.html')


def blog(request):
    return render(request, 'equipe.html')
