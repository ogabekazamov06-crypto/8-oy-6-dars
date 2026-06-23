from rest_framework import viewsets
from .models import CarBrand, Car, Comment
from .serializers import CarBrandSerializer, CarSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly, IsAuthorOrAdminOrReadOnly


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAdminOrReadOnly]

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Car.objects.all()
        brand_id = self.request.query_params.get('brand_id')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if brand_id: queryset = queryset.filter(brand_id=brand_id)
        if min_price: queryset = queryset.filter(price__gte=min_price)
        if max_price: queryset = queryset.filter(price__lte=max_price)
        return queryset



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrAdminOrReadOnly]




































# from rest_framework import generics
# from .models import CarBrand, Car,Comment
# from .serializers import CarBrandSerializer, CarSerializer, CommentSerializer
# from .permissions import IsAdminOrReadOnly, IsAuthorOrAdminOrReadOnly
#
#
# class CarBrandListCreateView(generics.ListCreateAPIView):
#     queryset = CarBrand.objects.all()
#     serializer_class = CarBrandSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
#
# class CarBrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CarBrand.objects.all()
#     serializer_class = CarBrandSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
# class CarListCreateView(generics.ListCreateAPIView):
#     serializer_class = CarSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
#     def get_queryset(self):
#         queryset = Car.objects.all()
#         brand_id = self.request.query_params.get('brand_id')
#         min_price = self.request.query_params.get('min_price')
#         max_price = self.request.query_params.get('max_price')
#         if brand_id is not None:
#             queryset = queryset.filter(brand_id=brand_id)
#         if min_price is not None:
#             queryset = queryset.filter(price__gte=min_price)
#         if max_price is not None:
#             queryset = queryset.filter(price__lte=max_price)
#         return queryset
#
#
# class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
#
# class CarListCreateView(generics.ListCreateAPIView):
#     serializer_class = CarSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
#     def get_queryset(self):
#         queryset = Car.objects.all()
#         brand_id = self.request.query_params.get('brand_id')
#         min_price = self.request.query_params.get('min_price')
#         max_price = self.request.query_params.get('max_price')
#
#         if brand_id: queryset = queryset.filter(brand_id=brand_id)
#         if min_price: queryset = queryset.filter(price__gte=min_price)
#         if max_price: queryset = queryset.filter(price__lte=max_price)
#         return queryset
#
#
# class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [IsAdminOrReadOnly]
#
# class CommentListCreateView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthorOrAdminOrReadOnly]
#
#
# class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthorOrAdminOrReadOnly]