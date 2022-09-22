from django.shortcuts import render


# Create your views here.

#def signlogin(request):print(request.POST)return render(request,'signup&login.html')

#def signlogin(request): return render(request,'signup&login.html')

def index(request):
 return render(request,'index.html')

def s17s(request):
    return render(request,'calc/2017_scheme.html')

def s18s(request):
    return render(request,'calc/2018_scheme.html')

def cgpa(request):
 return render(request,'cgpa.html')



def s17s1(request):
    return render(request,'calc/2017_scheme-1st_sem.html')

def s17s2(request):
    return render(request,'calc/2017_scheme-2nd_sem.html')

def s17s3(request):
    return render(request,'calc/2017_scheme-3rd_sem.html')

def s17s4(request):
    return render(request,'calc/2017_scheme-4th_sem.html')

def s17s5(request):
    return render(request,'calc/2017_scheme-5th_sem.html')

def s17s6(request):
    return render(request,'calc/2017_scheme-6th_sem.html')

def s17s7(request):
    return render(request,'calc/2017_scheme-7th_sem.html')


def s17s8(request):
    return render(request,'calc/2017_scheme-8th_sem.html')


def sgpa(request):
 return render(request,'sgpa.html')