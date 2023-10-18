from django.shortcuts import render
from .models import CoinList


def main(request):
    if request.method == "GET":
        context = {
            "data": CoinList.objects.values()
        }
        return render(request, 'app/main.html', context=context)
