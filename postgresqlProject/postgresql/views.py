from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Location, Petstore, Category, Employee, Breed, Customer, Sale
from .serializers import LocationSerializer, PetstoreSerializer, EmployeeSerializer, CategorySerializer, \
    BreedSerializer, CustomerSerializer, SaleSerializer
from .paginations import MyPageNumberPagination, MyCursorPagination, CustomPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'name': 'Pratik'})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        province = request.query_params.get('province')
        city = request.query_params.get('city')
        id = request.query_params.get('id')
        instances = self.queryset.filter(Q(province=province) | Q(city=city) | Q(id=id))
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.update(instance=instance, validated_data=serializer.validated_data)
            serializer = self.serializer_class(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PetstoreView(viewsets.ModelViewSet):
    queryset = Petstore.objects.all()
    serializer_class = PetstoreSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        instances = self.queryset
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.update(instance=instance, validated_data=serializer.validated_data)
            serializer = self.serializer_class(serializer)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        instance.delete()


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        instances = Employee.objects.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.update(instance=instance, validated_data=serializer.validated_data)
            serializer = self.serializer_class(serializer)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        instance.delete()


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        instances = Category.objects.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.update(instance=instance, validated_data=serializer.validated_data)
            serializer = self.serializer_class(serializer)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        instance.delete()


class BreedView(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        instances = Breed.objects.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.update(instance=instance, validated_data=serializer.validated_data)
            serializer = self.serializer_class(serializer)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        instance.delete()


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPagination
    # pagination_class = MyPageNumberPagination
    # pagination_class = LimitOffsetPagination
    # pagination_class = MyCursorPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        # instances = Customer.objects.all()
        self.queryset = Customer.objects.all()
        # serializer = self.serializer_class(instances, many=True)
        # return Response(serializer.data)
        return super().list(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.update(instance=instance, validated_data=serializer.validated_data)
            serializer = self.serializer_class(serializer)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.data.get('id')
        instance = self.queryset.get(id=id)
        instance.delete()


class SaleView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    # def get_object(self, id):
    #     try:
    #         return Sale.objects.get(id=id)
    #     except:
    #         raise status.HTTP_400_BAD_REQUEST

    def validate_ids(self, id_list):
        for id in id_list:
            try:
                Sale.objects.get(id=id)
            except:
                raise status.HTTP_400_BAD_REQUEST
        return True
    # def get_serializer_class(self):
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         return SaleSerializerWrite
    #
    #     return SaleSerializerRead

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     customer_dict = request.data['customer_dict']
    #     customer_serializer = CustomerSerializer(data=customer_dict)
    #     if customer_serializer.is_valid(raise_exception=True):
    #         customer = customer_serializer.save()
    #         request.data['customer'] = customer.id
    #         sale_serializer = self.get_serializer(data=request.data)
    #         if sale_serializer.is_valid(raise_exception=True):
    #              sale_serializer.save()
    #         headers = self.get_success_headers(sale_serializer.data)
    #         return Response(sale_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def create(self, request, *args, **kwargs):
    #     customer_dict = request.data['customer_dict']
    #     customer_serializer = CustomerSerializer(data=customer_dict)
    #     if customer_serializer.is_valid(raise_exception=True):
    #         customer = customer_serializer.save()
    #         sale_serializer = self.get_serializer(data=request.data, context={'customer': customer})
    #         if sale_serializer.is_valid(raise_exception=True):
    #             sale_serializer.save()
    #         headers = self.get_success_headers(sale_serializer.data)
    #         return Response(sale_serializer.data, status=status.HTTP_201_CREATED, headers=headers)



    # def retrieve(self, request, *args, **kwargs):
    #     id = request.data.get('id')
    #     instance = self.queryset.get(id=id)
    #     serializer = self.serializer_class(instance)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        sale = Sale.objects.select_related('employee').select_related('customer').get(id=id)
        sale_dict = {
            'id': sale.id,
            'employee': sale.employee.employee_name,
            'customer': sale.customer.customer_name,
            'breed': sale.breed.breed_name,
            'quantity': sale.quantity,
            'price': sale.total_price
        }
        return Response(sale_dict, status=status.HTTP_200_OK)

    # def list(self, request, *args, **kwargs):
    #     instances = Sale.objects.select_related('employee').select_related('customer')
    #     sale_list = []
    #     for instance in instances:
    #         sale_dict = {
    #             'id': instance.id,
    #             'employee': instance.employee.employee_name,
    #             'customer': instance.customer.customer_name,
    #             'breed': instance.breed.breed_name,
    #             'quantity': instance.quantity,
    #             'price': instance.total_price
    #         }
    #         sale_list.append(sale_dict)
    #
    #     return Response(sale_list, status=status.HTTP_200_OK)

    # def update(self, request, *args, **kwargs):
    #     id = request.data.get('id')
    #     instance = self.queryset.get(id=id)
    #     serializer = self.serializer_class(data=request.data, many=isinstance(request.data, list))
    #     if serializer.is_valid(raise_exception=True):
    #         sale = serializer.update(instance=instance, validated_data=serializer.validated_data)
    #         serializer = self.serializer_class(sale)
    #         return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        ids = [i['id'] for i in request.data]
        self.validate_ids(ids)
        instances = []
        for dic in request.data:
            id = dic['id']
            obj = self.get_object(id=id)
            obj.quantity = dic['quantity']
            obj.date = dic['date']
            obj.total_price = dic['total_price']
            obj.save()
            instances.append(obj)
        serializer = SaleSerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        customer = request.data.get('customer')
        instance = Customer.objects.get(id=customer)
        customer_serializer = CustomerSerializer(data=request.data['customer_dict'])
        if customer_serializer.is_valid(raise_exception=True):
            customer = customer_serializer.update(instance=instance, validated_data=customer_serializer.validated_data)
            id = request.data.get('id')
            instance = self.queryset.get(id=id)
            sale_serializer = self.get_serializer(data=request.data)
            if sale_serializer.is_valid(raise_exception=True):
                sale = sale_serializer.update(instance=instance, validated_data=sale_serializer.validated_data)
            #
            headers = self.get_success_headers(sale_serializer.data)
            return Response(sale_serializer.data, status=status.HTTP_200_OK, headers=headers)

    # def update(self, request, *args, **kwargs):
    #     customer = request.data.get('customer')
    #     customer_instance = Customer.objects.get(id=customer)
    #     customer_serializer = CustomerSerializer(data=request.data['customer_dict'])
    #     if customer_serializer.is_valid(raise_exception=True):
    #         customer = customer_serializer.update(instance=customer_instance, validated_data=customer_serializer.validated_data)
    #
    #     id = request.data.get('id')
    #     sale_instance = Sale.objects.get(id=id)
    #     sale_serializer = self.get_serializer(data=request.data)
    #     if sale_serializer.is_valid(raise_exception=True):
    #         sale = sale_serializer.update(instance=sale_instance, validated_data=sale_serializer.validated_data)
    #
    #
    #     headers = self.get_success_headers(sale_serializer.data)
    #     return Response(sale_serializer.data, status=status.HTTP_200_OK, headers=headers)


    # def delete(self, request, *args, **kwargs):
    #     id = request.data.get('id')
    #     instance = self.queryset.get(id=id)
    #     instance.delete()