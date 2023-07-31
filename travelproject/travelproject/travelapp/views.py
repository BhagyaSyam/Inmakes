from django.shortcuts import render

# Create your views here.
from .models import Place


#
# def demo(request):
#     obj=Place.objects.all()
#     return render(request, 'index.html',{'result':obj})


# {"obj": name})


def demo(request):
    obj = Place.objects.all()
    return render(request, 'index.html', {'result': obj})

# def about(request):
#     return render(request,'django.html')
#
#
#
# def contact(request):
#     return HttpResponse("hello am contact")
# def calculate(request):
#     X = int(request.GET["num1"])
#     Y = int(request.GET["num2"])
#     res = X + Y
#     res1 = X / Y
#     res2 = X * Y
#     res3 = X - Y
#
#     return render(request, "django.html", {"result": res , "results": res1 , "resultss": res2 , "resultsss": res3})
