from django.shortcuts import render
from .models import Project, Apartment, ApartmentImage, LatestProject
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.core.mail import send_mail
import json


def send_mail_num(number):
    send_mail(
        subject='Заявка на консультацию',
        message=f'Номер телефона: {number}.',
        from_email='psychotagcompany@gmail.com',
        recipient_list=['online@botanicaluxuryvillas.com'],
        fail_silently=False,
    )


def home(request):
    projects = Project.objects.all()
    latest_project = LatestProject.objects.all()[0]
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
        project.villas_design_quantity = str(project.villas_design_quantity)

        villa_ending = ''
        quantity = project.villas_quantity
        tens = ['11', '12', '13', '14', '15', '16', '17', '18', '19']

        if quantity[-2:] in tens:
            villa_ending = 'вилл'
        elif quantity[-1:] == '1':
            villa_ending = 'вилла'
        elif int(quantity[-1:]) > 1 and int(quantity[-1:]) < 5:
            villa_ending = 'виллы'
        else:
            villa_ending = 'вилл'
        project.villa_ending = villa_ending

        villa_design_ending = ''
        design_quantity = project.villas_design_quantity

        if design_quantity[-2:] in tens:
            villa_design_ending = 'дизайнов вилл'
        elif design_quantity[-1:] == '1':
            villa_design_ending = 'дизайн вилл'
        elif int(design_quantity[-1:]) > 1 and int(design_quantity[-1:]) < 5:
            villa_design_ending = 'дизайна вилл'
        else:
            villa_design_ending = 'дизайнов вилл'
        project.villa_design_ending = villa_design_ending

    return render(request, 'ru/home.html', {'projects': projects, 'latest_project': latest_project, })


# {% if project.villas_quantity == "1" %}
#                                     <div class="project__parameter">{{ project.villas_quantity }} вилл</div>
#                                 {% if project.villas_quantity|slice:"-1:" == "1" %}
#                                     <div class="project__parameter">{{ project.villas_quantity }} вилла</div>
#                                 {% elif project.villas_quantity|slice:"-1:" > "1" and project.villas_quantity|slice:"-1:" < "5" %}
#                                     <div class="project__parameter">{{ project.villas_quantity }} виллы</div>
#                                 {% else %}
#                                     <div class="project__parameter">{{ project.villas_quantity }} вилл</div>
#                                 {% endif %}

# {% if project.villas_design_quantity|slice:"-1:" == "1" %}
#                                 <div class="project__parameter">{{ project.villas_design_quantity }} дизайн вилл</div>
#                                 {% elif project.villas_design_quantity|slice:"-1:" > "1" and project.villas_design_quantity|slice:"-1:" < "5" %}
#                                 <div class="project__parameter">{{ project.villas_design_quantity }} дизайна вилл</div>
#                                 {% else %}
#                                 <div class="project__parameter">{{ project.villas_design_quantity }} дизайнов вилл</div>
#                                 {% endif %}

def about(request):
    projects = Project.objects.all()
    return render(request, 'ru/about.html', {'projects': projects})


def project_detail(request, slug):
    projects = Project.objects.all()
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

    if request.method == 'POST':
        send_mail_num(request.POST['phone'])

    return render(request, 'ru/project_detail.html', {"project": project, "projects": projects, "apartments": apartments})


def villa_detail(request, project_slug, pk):
    projects = Project.objects.all()
    project = Project.objects.get(slug=project_slug)
    villa = Apartment.objects.get(id=pk)
    apartment_images = ApartmentImage.objects.filter(apartment=pk)
    price = str(villa.price)
    # count = 0
    if len(price) > 6:
        villa.price = (price[-3:][::-1] + ' ' + price[-6:-3][::-1] + ' ' + price[-9:-6][::-1])[::-1]
    else:
        villa.price = (price[-3:][::-1] + ' ' + price[-6:-3][::-1])[::-1]

    if request.method == 'POST':
        send_mail_num(request.POST['phone'])

    return render(request, 'ru/villa_detail.html', {'villa': villa, 'project': project, "projects": projects, 'apartment_images': apartment_images,}) # 'count': count})


# def submit(request):
#     if request.method == 'POST':
#         print(request.POST)
#         return JsonResponse({"status": "success"})
#     return HttpResponse('bebebe')