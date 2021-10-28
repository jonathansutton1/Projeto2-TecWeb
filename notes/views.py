from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o app cjfinance do P2 de TecWeb!")
