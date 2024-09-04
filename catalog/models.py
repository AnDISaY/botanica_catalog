from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True)
    description = models.TextField()
    main_image = models.ImageField(upload_to='project/', default=' ')
    master_plan = models.ImageField()
    villas_quantity = models.PositiveSmallIntegerField()
    villas_design_quantity = models.PositiveSmallIntegerField()
    min_square = models.PositiveSmallIntegerField()
    max_square = models.PositiveSmallIntegerField()
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    video_url = models.CharField(max_length=400)
    map_iframe = models.TextField()

    def __str__(self):
        return self.title
    


class Parameter(models.Model):
    name = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.RESTRICT, related_name='parametres')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'parametres'


class Facility(models.Model):
    name = models.CharField(max_length=300)
    distance = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='facilities')
    
    def __str__(self):
        return f'{self.name}-{self.distance}m'
    
    class Meta:
        verbose_name_plural = 'facilities'
    

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project/images')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')



class Apartment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='apartments')
    name = models.CharField(max_length=4)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=10)
    bedroom = models.PositiveSmallIntegerField()
    bathroom = models.PositiveSmallIntegerField(default=0)
    square = models.PositiveSmallIntegerField()
    built_square = models.PositiveSmallIntegerField()
    house_square = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='project/apartments')

    def __str__(self):
        return self.name
    
        
class ApartmentImage(models.Model):
    image = models.ImageField(upload_to='apartment/images')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
