from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=150, unique=True, verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    date_created = models.DateField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True, blank= True)
    cvitae = models.ImageField(upload_to='cvitae/%y/%m/%d', null=True, blank= True)


    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'emplado'
        ordering = ['id']

    


