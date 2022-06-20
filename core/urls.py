from django. urls import path
# Llamar la vista de home, form de todos los objetos.
from.views import home, form_cliente, form_mod_cliente, form_del_cliente, form_producto, form_mod_producto, form_del_producto, form_medioPago, form_mod_medioPago, form_del_medioPago, form_venta, form_mod_venta, form_del_venta, form_detalleVenta, form_mod_detalleVenta, form_del_detalleVenta

# Se agrega  el formulario en las urls.py
urlpatterns = [
    path('',home,name='home'),
    path('form-cliente', form_cliente, name="form_cliente"),#FORMULARIO DE CREACIÓN CLIENTE
    path('form-mod-cliente/<id>', form_mod_cliente, name='form_mod_cliente'),#FORMULARIO DE MODIFICACIÓN CLIENTE
    path('form-del-cliente/<id>', form_del_cliente, name="form_del_cliente"),#FORMULARIO DE ELIMINACIÓN CLIENTE
    path('form-producto', form_producto, name="form_cliente"),#FORMULARIO DE CREACIÓN PRODUCTO
    path('form-mod-producto/<id>', form_mod_producto, name='form_mod_producto'),#FORMULARIO DE MODIFICACIÓN PRODUCTO
    path('form-del-producto/<id>', form_del_producto, name="form_del_producto"),#FORMULARIO DE ELIMINACIÓN PRODUCTO
    path('form-medioPago', form_medioPago, name="form_medioPago"),#FORMULARIO DE CREACIÓN MEDIO DE PAGO
    path('form-mod-medioPago/<id>', form_mod_medioPago, name='form_mod_medioPago'),#FORMULARIO DE MODIFICACIÓN MEDIO DE PAGO
    path('form-del-medioPago/<id>', form_del_medioPago, name="form_del_medioPago"),#FORMULARIO DE ELIMINACIÓN MEDIO DE PAGO
    path('form-venta', form_venta, name="form_venta"),#FORMULARIO DE CREACIÓN VENTA
    path('form-mod-venta/<id>', form_mod_venta, name='form_mod_venta'),#FORMULARIO DE MODIFICACIÓN VENTA
    path('form-del-venta/<id>', form_del_venta, name="form_del_venta"),#FORMULARIO DE ELIMINACIÓN VENTA
    path('form-detalleVenta', form_detalleVenta, name="form_detalleVenta"),#FORMULARIO DE CREACIÓN DETALLE DE VENTA
    path('form-mod-detalleVenta/<id>', form_mod_detalleVenta, name='form_mod_detalleVenta'),#FORMULARIO DE MODIFICACIÓN DETALLE DE VENTA
    path('form-del-detalleVenta/<id>', form_del_detalleVenta, name="form_del_detalleVenta"),#FORMULARIO DE ELIMINACIÓN DETALLE DE VENTA
]
