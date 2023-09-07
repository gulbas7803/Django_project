from django.shortcuts import render
from .models import CustomerData


# Create your views here.
def Displaying_Data(request):
    customers = CustomerData.objects.all()
    return render(request, 'Displaying_Data.html', {'customers': 'customres'})
