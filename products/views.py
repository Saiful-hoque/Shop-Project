from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
