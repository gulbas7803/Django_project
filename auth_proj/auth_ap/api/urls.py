from django.urls import path, include
from rest_framework import routers
from auth_ap.views import EmployeeCRUDCBV

router = routers.DefaultRouter()
router.register('employeeinfo', EmployeeCRUDCBV)

urlpatterns = [
    path('', include(router.urls)),
]
