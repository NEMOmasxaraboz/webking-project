from django.db import models


# Create your models here.


class Coffees(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(max_length=10)
    image = models.ImageField()
    info = models.CharField(max_length=450)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Coffees'
        verbose_name = 'Coffees'
        db_table = 'coffees'


class Cakes(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(max_length=10)
    image = models.ImageField()
    info = models.CharField(max_length=450)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cakes'
        verbose_name = 'Cakes'
        db_table = 'cakes'


class Complaints(models.Model):
    description = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Complaints'
        verbose_name = 'Complaint'
        db_table = 'complaints'
