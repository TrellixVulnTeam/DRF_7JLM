from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from newapp.models import Location, Petstore, Category, Employee, Breed, Customer, Sale
from newapp.serializers import LocationSerializer, PetstoreSerializer, EmployeeSerializer, CategorySerializer, \
    BreedSerializer, CustomerSerializer, SaleSerializer, SaleSerializer1Read, SaleSerializer2Read
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PetstoreView(viewsets.ModelViewSet):
    queryset = Petstore.objects.all()
    serializer_class = PetstoreSerializer


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BreedView(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SaleView1(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    # serializer_class = SaleSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SaleSerializer

        return SaleSerializer1Read

    # def list(self, request, *args, **kwargs):
    #     instances = Sale.objects.select_related('employee').select_related('breed')
    #     sale_list = []
    #     for instance in instances:
    #         sale_dict = {
    #             'id': instance.id,
    #             'employee_id': instance.employee.id,
    #             'breed_id': instance.breed.id,
    #             'breed_name': instance.breed.breed_name,
    #             'date': instance.date,
    #             'quantity': instance.quantity,
    #             'total_price': instance.total_price
    #         }
    #         sale_list.append(sale_dict)
    #
    #     return Response(sale_list, status=status.HTTP_200_OK)


class SaleView2(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    # serializer_class = SaleSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SaleSerializer

        return SaleSerializer2Read

    # def list(self, request, *args, **kwargs):
    #     query = Sale.objects.select_related('breed')
    #     ids = set([obj.breed.id for obj in query])
    #     dic = {}
    #     for id in ids:
    #         count = 0
    #         for value in Sale.objects.filter(breed=id):
    #             count = count+value.quantity
    #         dic[id] = count
    #     check = []
    #     sale_list = []
    #     instances = query
    #     for instance in instances:
    #         if instance.breed.id not in check:
    #             sale_dict = {
    #                 'breed_id': instance.breed.id,
    #                 'breed_name': instance.breed.breed_name,
    #                 'price': instance.breed.price,
    #                 'quantity': dic[instance.breed.id],
    #                 'total_price': instance.breed.price * dic[instance.breed.id]
    #             }
    #             sale_list.append(sale_dict)
    #             check.append(instance.breed.id)
    #     return Response(sale_list, status=status.HTTP_200_OK)


class SaleView3(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        date = request.query_params.get('date')
        query = Sale.objects.filter(date=date).select_related('breed')
        ids = set([obj.breed.id for obj in query])
        dic = {}
        for id in ids:
            count = 0
            for value in Sale.objects.filter(breed=id, date=date):
                count = count + value.quantity
            dic[id] = count
        check = []
        sale_list = []
        instances = query
        for instance in instances:
            if instance.breed.id not in check:
                sale_dict = {
                    'breed_id': instance.breed.id,
                    'quantity': dic[instance.breed.id],
                    'total_price': instance.breed.price * dic[instance.breed.id]
                }
                sale_list.append(sale_dict)
                check.append(instance.breed.id)
        return Response(sale_list, status=status.HTTP_200_OK)


class SaleView4(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        employee_id = request.query_params.get('employee_id')
        breed_id = request.query_params.get('breed_id')
        employee = Employee.objects.get(id=employee_id)
        breed = Breed.objects.get(id=breed_id)
        objects = Sale.objects.filter(employee=employee_id, breed=breed_id).select_related('customer')
        count = 0
        for o in objects:
            count = count+o.quantity
        quantity=count
        sale_dict = {
            'employee_id': employee_id,
            'employee_name': employee.employee_name,
            'breed_id': breed_id,
            'quantity': quantity,
            'total_price': quantity * breed.price,
        }
        customer_list = []
        for obj in objects:
            count = 0
            for o in Sale.objects.filter(customer=obj.customer.id, breed=breed_id):
                count = count+o.quantity
            q = count
            customer_dict = {
                'customer_id': obj.customer.id,
                'customer_name': obj.customer.customer_name,
                'quantity': q,
                'price': q * breed.price
            }
            customer_list.append(customer_dict)
        sale_dict['customer_info'] = customer_list
        return Response(sale_dict, status=status.HTTP_200_OK)


class SaleView5(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        query = Sale.objects.filter(date__range=[start_date, end_date]).select_related('breed')
        ids = set([obj.breed.id for obj in query])
        dic = {}
        for id in ids:
            dic[id] = Sale.objects.filter(breed=id, date__range=[start_date, end_date]).count()
        check = []
        sale_list = []
        instances = query
        for instance in instances:
            if instance.breed.id not in check:
                sale_dict = {
                    'breed_id': instance.breed.id,
                    'breed_name': instance.breed.breed_name,
                    'quantity': dic[instance.breed.id],
                    'total_price': instance.breed.price * dic[instance.breed.id]
                }
                sale_list.append(sale_dict)
                check.append(instance.breed.id)
        return Response(sale_list, status=status.HTTP_200_OK)


class SaleView6(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SaleView7(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        customer_dict = request.data['customer_dict']
        customer_serializer = CustomerSerializer(data=customer_dict)
        if customer_serializer.is_valid(raise_exception=True):
            customer = customer_serializer.save()
            request.data['customer'] = customer.id
            sale_serializer = self.get_serializer(data=request.data)
            if sale_serializer.is_valid(raise_exception=True):
                 sale_serializer.save()
            headers = self.get_success_headers(sale_serializer.data)
            return Response(sale_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
