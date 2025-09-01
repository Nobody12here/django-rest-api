from django.urls import path
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet, CategoryAPIView

router = SimpleRouter()
router.register("products", ProductViewSet, basename="product-viewset")
urlpatterns = [path("categories/", CategoryAPIView.as_view(), name="category-view")]
urlpatterns += router.urls
