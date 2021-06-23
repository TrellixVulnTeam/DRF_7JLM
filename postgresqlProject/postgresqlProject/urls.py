from django.contrib import admin
from django.urls import path, include
from postgresql import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('location', views.Location, 'location')
router.register('petstore', views.Petstore, 'petstore')
router.register('employee', views.Employee, 'employee')
router.register('category', views.Category, 'category')
router.register('breed', views.Breed, 'breed')
router.register('customer', views.Customer, 'customer')
router.register('sale', views.Sale, 'sale')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]