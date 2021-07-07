from django.contrib import admin
from django.urls import path, include
from postgresql import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

router = DefaultRouter()

router.register('locationview', views.LocationView, 'locationview')
router.register('petstoreview', views.PetstoreView, 'petstoreview')
router.register('employeeview', views.EmployeeView, 'employeeview')
router.register('categoryview', views.CategoryView, 'categoryview')
router.register('breedview', views.BreedView, 'breedview')
router.register('customerview', views.CustomerView, 'customerview')
router.register('saleview', views.SaleView, 'saleview')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
]