from django.shortcuts import render
from .models import HomeInfo, DemandInfo

# Create your views here.
def home_page(request):
    data = HomeInfo.objects.all()
    return render(request, 'myMainApp/page_home.html', {'data': data})


def salary_page(request):
    data = DemandInfo.objects.all()
    return render(request, 'myMainApp/salary_page.html', {'data': data})

