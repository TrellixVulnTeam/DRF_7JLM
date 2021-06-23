from rest_framework import viewsets
from .models import Location, Petstore, Category, Employee, Breed, Customer, Sale
from .serializers import LocationSerializer, PetstoreSerializer, EmployeeSerializer, CategorySerializer, \
    BreedSerializer, CustomerSerializer, SaleSerializer


class Location(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class Petstore(viewsets.ModelViewSet):
    queryset = Petstore.objects.all()
    serializer_class = PetstoreSerializer


class Employee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Breed(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class Customer(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Sale(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer