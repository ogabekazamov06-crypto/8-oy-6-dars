from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import CarBrand, Car, Comment
from .serializers import (CarBrandSerializer, CarSerializer, CarAdminSerializer, CommentSerializer)
from .permissions import MyIsAuthenticatedOrReadOnly


class CarBrandViewSet(ModelViewSet):
    queryset = CarBrand.objects.prefetch_related("cars")
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarApiViewSet(ModelViewSet):
    serializer_class = CarSerializer

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