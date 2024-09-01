from django import forms
from .models import Project, Parameter, Facility, Image


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'master_plan', 'villas_quantity', 'villas_design_quantity', 'min_square', 'max_square', 'min_price', 'max_price', 'video_url', 'map_iframe', 'paramet']