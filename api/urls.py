from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CarBrandViewSet, CarApiViewSet, CommentViewSet

router = DefaultRouter()
router.register('brands', CarBrandViewSet, basename='brand')
router.register('cars', CarApiViewSet, basename='car')
router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('cars/brand/<int:brand_id>/', CarApiViewSet.as_view({'get': 'list'})),

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]