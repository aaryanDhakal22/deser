from django.shortcuts import render, HttpResponse
from .gen_cords import gen_main


# Create your views here.
def homepage(request):
    locations = gen_main()
    return render(request, "dashboard/dashboard.html", context={"locations": locations})
