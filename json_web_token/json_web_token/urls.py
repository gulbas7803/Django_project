from django.contrib import admin
from django.urls import path, include
from web_token import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('studentapi',views.StudentViewSet, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshment/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify_token'),
]
