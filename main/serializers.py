from rest_framework import serializers
from . import models

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = "__all__"


class Repairs_and_servicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repairs_and_services
        fields = "__all__"


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Favorites
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Comment
        fields = "__all__"

