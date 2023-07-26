from django.shortcuts import render, redirect,HttpResponse

def index(request):
    return HttpResponse('SJHDJSDB')

def companyform(request):
    return render (request,'companyform.html')


def salesrepform(request):
    return render (request,'salesrep.html')



