from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentModel
from .forms import StdReader

# Create your views here.

def home(request):
    student_detil = StdReader(request.POST or None)
    if student_detil.is_valid():
        student_detil.save()
        return redirect('read')
    context= {'StdReader':StdReader}
    return render(request, 'home.html',context)

def read(request):
    studetail = StudentModel.objects.all()
    context = {'studetail':studetail}
    return render(request, 'read.html',context)

