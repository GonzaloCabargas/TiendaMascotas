from django.urls import path , include
from .views import *
from rest_framework import routers
from tienda.views import lista_producto, detalle_producto


router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', home, name="home"),
    path('tienda/', tienda, name="tienda"),
    path('registro/', registro, name="registro"),
    path('Contacto/', contacto, name="contacto"),
    path('donacion/', donacion, name="donacion"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('api/', include(router.urls)),
    path('api/', lista_producto, name="api"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto")
]
