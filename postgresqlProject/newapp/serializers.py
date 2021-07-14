from rest_framework import serializers
from .models import Location, Petstore, Category, Employee, Breed, Customer, Sale
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PetstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petstore
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.PrimaryKeyRelatedField(source='petstore.name', read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['id', 'category_name', 'name', 'petstore']
        # depth = 2


class EmployeeSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='employee_name')
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['id', 'empoyee_name', 'email', 'petstore', 'location']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'password2']
#
#     def validate(self, attrs):
#         print(attrs)
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError("Two passwords did not match")
#         return attrs
#
#     def create(self, validated_data):
#         print(validated_data)
#         hashed_password = validated_data['password']
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#         if validated_data['password'] != validated_data['password2']:
#             raise serializers.ValidationError("Two passwords did not match")
        # user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        # user.set_password(validated_data['password'])
        # user.save()
        # return user


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class SaleSerializer1Read(serializers.ModelSerializer):
    breed_name = serializers.PrimaryKeyRelatedField(source='breed.breed_name', read_only=True)
    employee_id = serializers.CharField(source='employee')
    breed_id = serializers.CharField(source='breed')
    class Meta:
        model = Sale
        fields = ['id', 'employee_id', 'breed_id', 'breed_name', 'date', 'quantity', 'total_price']


class SaleSerializer2Read(serializers.ModelSerializer):
    breed_id = serializers.CharField(source='breed')
    breed_name = serializers.PrimaryKeyRelatedField(source='breed.breed_name', read_only=True)
    price = serializers.PrimaryKeyRelatedField(source='breed.price', read_only=True)
    class Meta:
        model = Sale
        fields = ['breed_id', 'breed_name', 'price']




