from django.contrib import admin
from django.urls import path, include
from postgresql import views as postgresql_views
from newapp import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

router = DefaultRouter()

router.register('locationview', views.LocationView, 'locationview')
router.register('petstoreview', views.PetstoreView, 'petstoreview')
router.register('employeeview', views.EmployeeView, 'employeeview')
router.register('categoryview', views.CategoryView, 'categoryview')
router.register('breedview', views.BreedView, 'breedview')
router.register('customerview', views.CustomerView, 'customerview')
router.register('saleview1', views.SaleView1, 'saleview1')
router.register('saleview2', views.SaleView2, 'saleview2')
router.register('saleview3', views.SaleView3, 'saleview3')
router.register('saleview4', views.SaleView4, 'saleview4')
router.register('saleview5', views.SaleView5, 'saleview5')
router.register('saleview6', views.SaleView6, 'saleview6')
router.register('registerview', postgresql_views.RegisterView, 'registerview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]