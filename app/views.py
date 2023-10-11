from django.shortcuts import render
from .models import Truck

# Create your views here.
def automobil(request):
    trucks = Truck.objects.values('brand', 'engine')
    return render(request, 'index.html', {'trucks': trucks})

