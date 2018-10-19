from django.shortcuts import render
from .models import component

# Create your views here.
def List(request):
    a=component.objects.all()
    return render(request,'components\Base.html',{'a':a})