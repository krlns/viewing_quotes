from django.shortcuts import render
from .models import CompanyList


def main(request):
    if request.method == "GET":
        context = {
            "data": CompanyList.objects.values()
        }
        return render(request, 'app/main.html', context=context)
