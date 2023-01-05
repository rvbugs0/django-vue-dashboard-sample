from django.shortcuts import render


# Create your views here.
def table_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "table.html")

def chart_view(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "chart.html")

def index_view(request):
    return render(request,"index.html")