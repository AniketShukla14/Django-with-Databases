from django.shortcuts import render
from .models import member
def home(request):
    all_members=member.objects.all
    return render(request,'home.html',{'all':all_members})