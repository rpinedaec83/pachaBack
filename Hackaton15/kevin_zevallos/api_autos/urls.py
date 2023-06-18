from django.urls import include,path
from rest_framework import routers
from .views import TipoViewSet,MarcaViewSet,AutoViewSet
router = routers.DefaultRouter()
router.register('api/tipo',TipoViewSet,'tipos')
router.register('api/marca',TipoViewSet,'marcas')
router.register('api/auto',TipoViewSet,'autos')
urlpatterns=[
    path('',include(router.urls)),
]


