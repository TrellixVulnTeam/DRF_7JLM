from rest_framework import serializers
from .models import Location, Petstore, Category, Employee, Breed, Customer, Sale
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
import re


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
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'password2']

    def validate(self, attrs):
        specialsym = ['!', '@', '#', '$', '%', '&']

        if not re.search(r"[\d]+", attrs['password']):
            raise serializers.ValidationError("The password must contain at least one digit")

        if not re.search(r"[A-Z]+", attrs['password']):
            raise serializers.ValidationError("The password must contain at least one uppercase character")

        if not any(char in specialsym for char in attrs['password']):
            raise serializers.ValidationError("The password must contain at least one special character")

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Two passwords did not match")

        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    # def create(self, validated_data):
    #     return Sale.objects.create(**validated_data)


    # def create(self, validated_data):
    #     print(validated_data)
    #     validated_data.pop('customer')
    #     print(validated_data)
    #     instance = self.Meta.model.objects.create(customer=self.context['customer'], **validated_data)
    #     return instance

    # def update(self, instance, validated_data):
    #     instance.employee = validated_data.get('employee', instance.employee)
    #     instance.customer = validated_data.get('customer', instance.customer)
    #     instance.breed = validated_data.get('breed', instance.breed)
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.total_price = validated_data.get('total_price', instance.total_price)
    #     instance.save()
    #     return instance


