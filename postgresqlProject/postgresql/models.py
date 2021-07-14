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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField()
    petstore = models.ForeignKey(Petstore, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    petstore = models.ForeignKey(Petstore, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


class Breed(models.Model):
    breed_name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.breed_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Sale(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    total_price = models.IntegerField()


from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )