from rest_framework import serializers
from .models import Location, Petstore, Category, Employee, Breed, Customer, Sale


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = self.context['name']
        return representation

# create both; sending context
# update retrieve both
# serializer method change upper, float
class PetstoreSerializer(serializers.ModelSerializer):
    # location = LocationSerializer()
    class Meta:
        model = Petstore
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # petstore = PetstoreSerializer()
    name = serializers.PrimaryKeyRelatedField(source='petstore.name', read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'name', 'petstore']
        depth = 2


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


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        return Sale.objects.create(**validated_data)


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
