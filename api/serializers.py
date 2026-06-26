from rest_framework import serializers
from .models import CarBrand, Car, Comment


class CarSerializerForBrand(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['brand']


class CarBrandSerializer(serializers.ModelSerializer):
    cars = CarSerializerForBrand(many=True, read_only=True)

    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'country', 'cars']



class BrandSerializerForCar(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    brend = BrandSerializerForCar(read_only=True, source='brand')

    class Meta:
        model = Car
        fields = '__all__'
        extra_kwargs = {'brand': {'write_only': True}} # Ma'lumot kiritganda faqat ID yuboriladi


class CarAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'car', 'text']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)