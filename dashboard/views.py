from main.models import Car, Repairs_and_services, Photo, Tag
from main.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def create_car(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        photo = request.POST.getlist('photo')
        brand = request.POST.get('brand')
        region = request.POST.get('region')
        engine_capacity = request.POST.get('engine_capacity')
        year = request.POST.get('year')
        is_automat = request.POST.get('is_automat')
        phone_number = request.POST.get('phone_number')
        description = request.POST.get('description')
        is_rent = request.POST.get('is_rent')
        mileage = request.POST.get('mileage')
        addition = request.POST.get('addition')
        view = request.POST.get('view')
        is_active = request.POST.get('is_active')
        position = request.POST.get('position')
        tag = request.POST.getlist('tag')
        district = request.POST.get('district')
        is_light = request.POST.get('is_light')
        lat = request.POST.get('lat')
        lot = request.POST.get('lot')
        is_bargaining = request.POST.get('is_bargaining')
        new_car = Car.objects.create(
            name=name,
            price=price,
            brand_id=brand,
            region_id=region,
            engine_capacity=engine_capacity,
            year=year,
            is_automat=is_automat,
            phone_number=phone_number,
            description=description,
            is_rent=is_rent,
            mileage=mileage,
            addition=addition,
            view=view,
            is_active=is_active,
            position=position,
            district_id=district,
            is_light=is_light,
            lat=lat,
            lot=lot,
            is_bargaining=is_bargaining,
        )
        for i in tag:
            new_car.tag.add(i)
            new_car.save()
        for i in photo:
            new_car.photo.add(i)
            new_car.save()
        ser = CarSerializer(new_car)
        return Response(ser.data)


@api_view(['PUT'])
def update_car(request, pk):
    car = Car.objects.get(pk=pk)
    name = request.POST.get('name')
    price = request.POST.get('price')
    photo = request.FILES.getlist('photo')
    brand = request.POST.get('brand')
    region = request.POST.get('region')
    engine_capacity = request.POST.get('engine_capacity')
    year = request.POST.get('year')
    is_automat = request.POST.get('is_automat')
    phone_number = request.POST.get('phone_number')
    description = request.POST.get('description')
    is_rent = request.POST.get('is_rent')
    mileage = request.POST.get('mileage')
    addition = request.POST.get('addition')
    view = request.POST.get('view')
    is_active = request.POST.get('is_active')
    position = request.POST.get('position')
    tag = request.POST.getlist('tag')
    district = request.POST.get('district')
    is_light = request.POST.get('is_light')
    lat = request.POST.get('lat')
    lot = request.POST.get('lot')
    is_bargaining = request.POST.get('is_bargaining')
    car.car = car
    car.name = name
    car.price = price
    car.brand.id = brand
    car.region.id = region
    car.engine_capacity = engine_capacity
    car.year = year
    car.is_automat = is_automat
    car.phone_number = phone_number
    car.description = description
    car.is_rent = is_rent
    car.mileage = mileage
    car.addition = addition
    car.view = view
    car.is_active = is_active
    car.position = position
    car.district.id = district
    car.is_light = is_light
    car.lat = lat
    car.lot = lot
    car.is_bargaining = is_bargaining
    if photo is not None:
        for i in photo:
            photo = Photo.objects.create(
                image=i
            )
            car.photo.add(photo)
    car.save()
    ser = CarSerializer(car)
    return Response(ser.data)



@api_view(["DELETE"])
def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return Response({'message': "Deleted"})


@api_view(['POST'])
def create_repairs_and_services(request):
    if request.method == "POST":
        photo = request.POST.getlist('photo')
        phone_number = request.POST.get('phone_number')
        type_repairs = request.POST.get('type_repairs')
        lat = request.POST.get('lat')
        lot = request.POST.get('lot')
        region = request.POST.get('region')
        description = request.POST.get('description')
        addition = request.POST.get('addition')
        new_repairs_and_services = Repairs_and_services.objects.create(
            phone_number=phone_number,
            type_repairs=type_repairs,
            lat=lat,
            lot=lot,
            region_id=region,
            description=description,
            addition=addition,
        )
        for i in photo:
            new_repairs_and_services.photo.add(i)
            new_repairs_and_services.save()
        ser = Repairs_and_servicesSerializer(new_repairs_and_services)
        return Response(ser.data)


@api_view(['PUT'])
def update_repairs_and_services(request, pk):
    repairs_and_services = Repairs_and_services.objects.get(pk=pk)
    photo = request.FILES.getlist('photo')
    phone_number = request.POST.get('phone_number')
    type_repairs = request.POST.get('type_repairs')
    lat = request.POST.get('lat')
    lot = request.POST.get('lot')
    region = request.POST.get('region')
    description = request.POST.get('description')
    addition = request.POST.get('addition')
    repairs_and_services.repairs_and_services = repairs_and_services
    repairs_and_services.phone_number = phone_number
    repairs_and_services.type_repairs = type_repairs
    repairs_and_services.lat = lat
    repairs_and_services.lot = lot
    repairs_and_services.region = region
    repairs_and_services.description = description
    repairs_and_services.addition = addition
    if photo is not None:
        for i in photo:
            photo = Photo.objects.create(
                image=i
            )
            repairs_and_services.photo.add(photo)
    repairs_and_services.save()
    ser = Repairs_and_servicesSerializer(repairs_and_services)
    return Response(ser.data)


@api_view(["DELETE"])
def delete_repairs_and_services(request, pk):
    repairs_and_services = Repairs_and_services.objects.get(pk=pk)
    repairs_and_services.delete()
    return Response({'message': "Deleted"})