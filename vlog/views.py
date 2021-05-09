from django.shortcuts import render
from django.http import HttpResponse
from .models import blogs
# Create your views here.
blog1=blogs()
blog1.name='share'
blog1.short_desc="kuch bhi likh rha"

def home(request):
    return render(request,'index.html',{'blog1':blog1})