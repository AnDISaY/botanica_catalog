from django.contrib import admin
from .models import Project, Parameter, Facility, Image, Apartment


class ParameterInline(admin.TabularInline):
    model = Parameter


class FacilityInline(admin.TabularInline):
    model = Facility


class ImageInline(admin.TabularInline):
    model = Image


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ParameterInline, FacilityInline, ImageInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Apartment)
