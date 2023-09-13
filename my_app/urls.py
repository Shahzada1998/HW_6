

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('departments', views.DepartmentViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('positions', views.PositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/department/<int:pk>/employees/', views.DepartmentEmployeesViewSet.as_view({'get': 'list'}))

]