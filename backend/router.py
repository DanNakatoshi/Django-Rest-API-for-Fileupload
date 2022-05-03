from fileupload.views import StoreDocViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('store-doc', StoreDocViewSet)

