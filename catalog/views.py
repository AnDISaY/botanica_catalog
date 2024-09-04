from django.shortcuts import render
from .models import Project, Apartment
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
import json


def home(request):
    projects = Project.objects.all()
    for project in projects:
        min_price = str(project.min_price)
        max_price = str(project.max_price)
        if len(min_price) > 6:
            project.min_price = (min_price[-3:][::-1] + ' ' + min_price[-6:-3][::-1] + ' ' + min_price[-9:-6][::-1])[::-1]
        else:
            project.min_price = (min_price[-3:][::-1] + ' ' + min_price[-6:-3][::-1])[::-1]
        if len(max_price) > 6:
            project.max_price = (max_price[-3:][::-1] + ' ' + max_price[-6:-3][::-1] + ' ' + max_price[-9:-6][::-1])[::-1]
        else:
            project.max_price = (max_price[-3:][::-1] + ' ' + max_price[-6:-3][::-1] )[::-1]
        project.villas_quantity = str(project.villas_quantity)
    return render(request, 'home.html', {'projects': projects})


def about(request):
    return render(request, 'about.html')


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    apartments = list(project.apartments.all())
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        bedroom = request.POST['number-radio']
        max_price = request.POST['price-number']
        max_square = request.POST['square-number']
        if bedroom == '4':
            apartmentsf = project.apartments.filter(bedroom__gte=bedroom, price__range=(0, max_price), square__range=(0, max_square))
        else:
            apartmentsf = project.apartments.filter(bedroom=bedroom, price__range=(0, max_price), square__range=(0, max_square))
        serialized_data = serialize("json", apartmentsf)
        serialized_data = json.loads(serialized_data)
        return JsonResponse({"apartmentsf": serialized_data})
    return render(request, 'project_detail.html', {"project": project, "apartments": apartments})


def villa_detail(request, project_slug, pk):
    project = Project.objects.get(slug=project_slug)
    villa = Apartment.objects.get(id=pk)
    price = str(villa.price)
    # count = 0
    if len(price) > 6:
        villa.price = (price[-3:][::-1] + ' ' + price[-6:-3][::-1] + ' ' + price[-9:-6][::-1])[::-1]
    else:
        villa.price = (price[-3:][::-1] + ' ' + price[-6:-3][::-1])[::-1]
    # price = price[-6:-3]
    # print(price)
    # print(price[-6:-3][::-1])
    return render(request, 'villa_detail.html', {'villa': villa, 'project': project,}) # 'count': count})


# def submit(request):
#     if request.method == 'POST':
#         print(request.POST)
#         return JsonResponse({"status": "success"})
#     return HttpResponse('bebebe')