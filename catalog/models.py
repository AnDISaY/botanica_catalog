from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(primary_key=True, verbose_name="Ссылка (slug)")
    description = models.TextField(verbose_name="Описание")
    main_image = models.ImageField(upload_to='project/', default=' ', verbose_name="Главное изображение")
    master_plan = models.ImageField(verbose_name="Название")
    villas_quantity = models.PositiveSmallIntegerField(verbose_name="Кол-во вилл")
    villas_design_quantity = models.PositiveSmallIntegerField(verbose_name="Кол-во дизайнов вилл")
    min_square = models.PositiveSmallIntegerField(verbose_name="Мин. площадь")
    max_square = models.PositiveSmallIntegerField(verbose_name="Макс. площадь")
    min_price = models.PositiveIntegerField(verbose_name="Мин. цена")
    max_price = models.PositiveIntegerField(verbose_name="Макс. цена")
    video_url = models.CharField(max_length=400, verbose_name="Ссылка на видео")
    map_iframe = models.TextField(verbose_name="Ссылка на карту")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    


class Parameter(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='parametres', null=True, verbose_name="Проект")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Параметры'


class Facility(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    distance = models.PositiveIntegerField(verbose_name="Расстояние")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='facilities', verbose_name="Проект")
    
    def __str__(self):
        return f'{self.name}-{self.distance}m'
    
    class Meta:
        verbose_name_plural = 'Удобства'
    

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project/images', verbose_name="Изображение")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="Проект")



class Apartment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='apartments', verbose_name="Проект")
    name = models.CharField(max_length=4, verbose_name="Название")
    description = models.CharField(max_length=100, verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    type = models.CharField(max_length=10, verbose_name="Тип")
    bedroom = models.PositiveSmallIntegerField(verbose_name="Кол-во спален")
    bathroom = models.PositiveSmallIntegerField(default=0, verbose_name="Кол-во ванн")
    square = models.PositiveSmallIntegerField(verbose_name="Площадь")
    built_square = models.PositiveSmallIntegerField(verbose_name="Застроено")
    house_square = models.PositiveSmallIntegerField(verbose_name="Площадь виллы")
    image = models.ImageField(upload_to='project/apartments', verbose_name="Изображение")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Вилл"
        verbose_name_plural = "Виллы"
    
        
class ApartmentImage(models.Model):
    image = models.ImageField(upload_to='apartment/images', verbose_name="Изображение")
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images', verbose_name="Вилла")
