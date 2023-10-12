from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Photo(models.Model):
    image = models.ImageField(upload_to='photo_car', verbose_name="Rasm")


class Brand(models.Model):
    name = models.CharField(max_length=55, verbose_name='Brend nomi')

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=25, verbose_name="Viloyat nomi")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    photo = models.ManyToManyField(to=Photo)
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT, verbose_name="Brendi")
    region = models.ForeignKey(to=Region,on_delete=models.CASCADE, verbose_name="Viloyat nomi")
    engine_capacity = models.IntegerField(default=1)
    year = models.IntegerField(default=2023, verbose_name="Chiqqan yili")
    is_automat = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=13)
    description = models.TextField()
    is_rent = models.BooleanField(default=False)
    mileage = models.IntegerField(default=1)
    addition = models.TextField(null=True, blank=True)
    view = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    position = models.IntegerField(default=1)
    tag = models.ManyToManyField(to=Tag)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    is_light = models.BooleanField(default=True)
    lat = models.DecimalField(max_digits=10, decimal_places=2)
    lot = models.DecimalField(max_digits=10, decimal_places=2)
    is_bargaining = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Repairs_and_services(models.Model):
    photo = models.ManyToManyField(to=Photo)
    phone_number = models.CharField(max_length=13)
    type_repairs = models.CharField(max_length=255, verbose_name="Avtoservis nomi")
    lat = models.DecimalField(max_digits=7, decimal_places=2)
    lot = models.DecimalField(max_digits=7, decimal_places=2)
    region = models.ForeignKey(to=Region, on_delete=models.PROTECT, verbose_name="Viloyati")
    description = models.TextField()
    addition = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.type_repairs


class Favorites(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cars = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Soni')

    def __str__(self):
        return self.cars.name


class Comment(models.Model):
    comment = models.ForeignKey(to='Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    text = models.TextField(verbose_name='izoh')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.name

