
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CarBrandViewSet, CarViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'brands', CarBrandViewSet, basename='brand')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/token/', obtain_auth_token, name='obtain_token'),
]
# from django.urls import path
# # from .views import (
# #     CarBrandListCreateView, CarBrandRetrieveUpdateDestroyView,
# #     CarListCreateView, CarRetrieveUpdateDestroyView,
# #     CommentListCreateView, CommentRetrieveUpdateDestroyView
# # )
#
# urlpatterns = [
#     path('api/brands/', CarBrandListCreateView.as_view(), name='brand_list_create'),
#     path('api/brands/<int:pk>/', CarBrandRetrieveUpdateDestroyView.as_view(), name='brand_detail'),
#     path('api/cars/', CarListCreateView.as_view(), name='car_list_create'),
#     path('api/cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car_detail'),
#
#     path('api/comments/', CommentListCreateView.as_view(), name='comment_list_create'),
#     path('api/comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_detail'),
# ]