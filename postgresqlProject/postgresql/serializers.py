from rest_framework import serializers
from .models import Location, Petstore, Category, Employee, Breed, Customer, Sale


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PetstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petstore
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'petstore']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_name', 'email', 'petstore', 'location']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'