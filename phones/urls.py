from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    CategoryListCreateView,
    ProductDetailView,
    ProductFilterView,
    ProductByCategoryView,
)

urlpatterns = [
    path('products/filter/', ProductFilterView.as_view(), name='product-filter'),  # Для фильтрации всех продуктов
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', ProductFilterView.as_view(), name='products'),
    path('products/<slug:slug>/', ProductByCategoryView.as_view(), name='products'),

    path('products/<slug:slug>/filter/', ProductFilterView.as_view(), name='product-filter-by-category'),

      # Для фильтрации по категории
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)