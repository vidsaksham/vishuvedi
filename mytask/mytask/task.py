from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def setvalue(request):
    d1 = request.GET.get('d1')
    t1 = request.GET.get('t1')
    t2 = request.GET.get('t2')
    t3 = request.GET.get('t3')
    t4 = request.GET.get('t4')
    t5 = request.GET.get('t5')
    t6 = request.GET.get('t6')
    params = { 'd1' : d1 , 't1':t1 ,'t2' : t2 ,'t3' : t3 ,'t4' : t4 ,'t5' : t5 ,  't6' : t6 }
    return render(request, 'create.html' , params )