from django.urls import path
from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet

router = SimpleRouter()
router.register("products", ProductViewSet, basename="product-viewset")
urlpatterns = router.urls
