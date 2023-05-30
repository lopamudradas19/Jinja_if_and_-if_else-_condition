from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name' : 'raj'}
    return render(request,'wish.html',context=d)

def conditions(request):
    d={'a' : 10,'b':19}
    return render(request,'conditions.html',context=d)

