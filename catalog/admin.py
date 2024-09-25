from django.contrib import admin
from .models import Project, Parameter, Facility, ProjectImage, Apartment, ApartmentImage


class ParameterInline(admin.TabularInline):
    model = Parameter


class FacilityInline(admin.TabularInline):
    model = Facility


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ParameterInline, FacilityInline, ProjectImageInline]


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage


class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Apartment, ApartmentAdmin)
