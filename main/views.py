from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(['GET'])
def get_all_car(request):
    cars = models.Car.objects.filter(is_active=True)
    ser = serializers.CarSerializer(cars, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_all_repairs_and_services(request):
    repairs_and_services = models.Repairs_and_services.objects.all()
    ser = serializers.Repairs_and_servicesSerializer(repairs_and_services, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_car_by_region(request, pk):
    region = models.Region.objects.get(pk=pk)
    cars = models.Car.objects.filter(region=region)
    ser = serializers.CarSerializer(cars, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_car_by_district(request, pk):
    district = models.District.objects.get(pk=pk)
    cars = models.Car.objects.filter(district=district)
    ser = serializers.CarSerializer(cars, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_repairs_and_services_by_region(request, pk):
    region = models.Region.objects.get(pk=pk)
    repairs_and_services = models.Repairs_and_services.objects.filter(region=region)
    ser = serializers.Repairs_and_servicesSerializer(repairs_and_services, many=True)
    return Response(ser.data)


@api_view(['POST'])
def search_car_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        car = models.Car.objects.filter(name__icontains=name)
        ser = serializers.CarSerializer(car, many=True)
        return Response(ser.data)


@api_view(['POST'])
def search_repairs_and_services_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        repairs_and_services = models.Repairs_and_services.objects.filter(name__icontains=name)
        ser = serializers.Repairs_and_servicesSerializer(repairs_and_services, many=True)
        return Response(ser.data)


@api_view(['GET'])
def filter_car_by_rent(request):
    car = models.Car.objects.filter(is_rent=True)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_not_rent(request):
    car = models.Car.objects.filter(is_rent=False)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_light(request):
    car = models.Car.objects.filter(is_light=True)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_not_light(request):
    car = models.Car.objects.filter(is_light=False)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_bargaining(request):
    car = models.Car.objects.filter(is_bargaining=True)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_not_bargaining(request):
    car = models.Car.objects.filter(is_bargaining=False)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_automat(request):
    car = models.Car.objects.filter(is_automat=True)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_car_by_mechanic(request):
    car = models.Car.objects.filter(is_automat=False)
    ser = serializers.CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(['POST'])
def add_favorites_car(request, pk):
    car = models.Car.objects.get(pk=pk)
    favorites_car = models.Favorites.objects.create(
        user=request.user,
        car=car
    )
    ser = serializers.FavoritesSerializer(favorites_car)
    return Response(ser.data)


@api_view(['POST'])
def add_favourites_repairs_and_services(request, pk):
    repairs_and_services = models.Repairs_and_services.objects.filter(pk=pk)

    favorites_repairs_and_services = models.Favorites.objects.create(
        user=request.user,
        repairs_and_services=repairs_and_services
    )
    ser = serializers.FavoritesSerializer(favorites_repairs_and_services)
    return Response(ser.data)


@api_view(['GET'])
def get_all_favourites(request):
    car = models.Favorites.objects.filter(user=request.user)
    ser = serializers.FavoritesSerializer(car, many=True)
    return Response(ser.data)


@api_view(['PUT'])
def update_cars_view(request, pk):
    car = models.Car.objects.get(pk=pk)
    car.view += 1
    car.save()
    ser = serializers.CarSerializer(car)
    return Response(ser.data)


@api_view(['POST'])
def create_comment(request, pk):
    car = models.Car.objects.get(pk=pk)
    if request.method == "POST":
        text = request.POST['text']
        comment = models.Comment.objects.create(
            text=text,
            user=request.user,
            car=car
        )
        ser = serializers.CarSerializer(comment)
        return Response(ser.data)


@api_view(['POST'])
def reply_comment(request, pk):
    car = models.Car.objects.get(pk=pk)
    comment_id = request.POST.get('comment_id')
    text = request.POST['text']
    user = request.user
    new_comment = models.Comment.objects.create(
        user=user,
        car_id=car,
        text=text,
        comment_id=comment_id,
    )
    ser = serializers.CommentSerializer(new_comment)
    return Response(ser.data)



