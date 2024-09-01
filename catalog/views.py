from django.shortcuts import render
from .models import Project
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
import json


def home(request):
    projects = Project.objects.all()
    for project in projects:
        project.villas_quantity = str(project.villas_quantity)
    return render(request, 'home.html', {'projects': projects})


def about(request):
    return render(request, 'about.html')


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    apartments = list(project.apartments.all())
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        bedroom = request.POST['number-radio']
        min_price = request.POST.getlist('price-number')[0]
        max_price = request.POST.getlist('price-number')[1]
        min_square = request.POST.getlist('square-number')[0]
        max_square = request.POST.getlist('square-number')[1]
        if bedroom == '4':
            apartmentsf = project.apartments.filter(bedroom__gte=bedroom, price__range=(min_price, max_price), square__range=(min_square, max_square))
        else:
            apartmentsf = project.apartments.filter(bedroom=bedroom, price__range=(min_price, max_price), square__range=(min_square, max_square))
        print(apartmentsf)
        serialized_data = serialize("json", apartmentsf)
        serialized_data = json.loads(serialized_data)
        return JsonResponse({"apartmentsf": serialized_data})
    return render(request, 'project_detail.html', {"project": project, "apartments": apartments})


# def submit(request):
#     if request.method == 'POST':
#         print(request.POST)
#         return JsonResponse({"status": "success"})
#     return HttpResponse('bebebe')