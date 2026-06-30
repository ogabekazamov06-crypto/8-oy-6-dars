from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import CarBrand, Car, Comment
from .serializers import (CarBrandSerializer, CarSerializer, CarAdminSerializer, CommentSerializer)
from .permissions import MyIsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class BrandPageNumberPagination(PageNumberPagination):
    page_size = 5



class CarLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5



class CommentCursorPagination(CursorPagination):
    page_size = 5
    ordering = '-created_at'


class CarBrandViewSet(ModelViewSet):
    queryset = CarBrand.objects.prefetch_related("cars")
    serializer_class = CarBrandSerializer


    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'country']
    filterset_fields = ['country']

    pagination_class = BrandPageNumberPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]


class CarApiViewSet(ModelViewSet):
    serializer_class = CarSerializer
    pagination_class = CarLimitOffsetPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        brand_id = self.kwargs.get("brand_id")

        menu = self.request.query_params.get('menu')
        menu_response = True if menu == 'on' else False if menu == 'off' else None
        base_queryset = Car.objects.select_related('brand') \
            .prefetch_related('comments') \
            .only('id', 'model_name', 'price', 'brand_id', 'add_menu') \
            .defer('color', 'year')

        if brand_id:
            queryset = base_queryset.filter(brand_id=brand_id)
        else:
            queryset = base_queryset.all()

        if menu_response in [True, False]:
            queryset = queryset.filter(add_menu=menu_response)

        return queryset

    def get_serializer_class(self):
        if self.request.user and self.request.user.is_staff:
            return CarAdminSerializer
        return self.serializer_class


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.select_related('car', 'user')
    serializer_class = CommentSerializer
    permission_classes = [MyIsAuthenticatedOrReadOnly]
    pagination_class = CommentCursorPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]