from django.db import models


class Location(models.Model):
    province = models.IntegerField()
    city = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)

    def __str__(self):
        return self.city


class Petstore(models.Model):
    name = models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    petstore = models.ForeignKey(Petstore, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    petstore = models.ForeignKey(Petstore, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


class Breed(models.Model):
    breed_name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)


class Sale(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    total_price = models.IntegerField()