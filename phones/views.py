from rest_framework import generics
from .models import Category, Product
from phones.serializer import CategorySerializer, ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('slug', None)
        return Product.objects.filter(category__slug=category_slug)

class ProductFilterView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs.get('slug', None)

        queryset = Product.objects.all()
        if category_slug:
            queryset = Product.objects.filter(category__slug=category_slug)



        price = self.request.query_params.get('price')
        ram = self.request.query_params.get('ram')
        storage = self.request.query_params.get('storage')

        if price and price.isdigit():
            queryset = queryset.filter(price__lte=int(price))
        if ram:
            # Если ram передан как строка с числами, например, '4', то фильтруем по точному значению
            queryset = queryset.filter(ram__exact=ram)
        if storage:
            queryset = queryset.filter(storage__in=storage.split(','))

        return queryset

