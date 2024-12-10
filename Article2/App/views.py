from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    data=Article.objects.all()
    context={
        'data':data
    }
    return render(request,'index.html',context)
def result(request,Hari):
    data1=Article.objects.get(id=Hari)
    context={
        'data1':data1
    }
    return render(request,'Result.html',context)
