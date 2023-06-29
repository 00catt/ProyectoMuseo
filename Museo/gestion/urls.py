from . import views
from django.urls import path
urlpatterns =[
     path('', views.home, name='home'),
    path('validacion/', views.val, name='validacion'),
    path('arte/', views.art, name='arte'),
    path('colores/', views.col, name='colores'),
    path('creacion/', views.crea, name='creacion'),
    path('elgrito/', views.elg, name='elgrito'),
    path('japones/', views.jap, name='japones'),
    path('pinturas/', views.pint, name='pinturas'),
    path('sobre/', views.sobr, name='sobre'),
    path('curso/', views.cur, name='curso'),
    path('Artista/', views.rear, name='registro'),
    path('registrarArtista/', views.registrarArtista),
    path('editarArtista/<codigo>', views.editarArtista),
    path('edicionArtista/', views.edicionArtista),
    path('eliminarArtista/<codigo>', views.eliminarArtista),
    
    path('adproductos/', views.adpro, name='adproductos'),
    path('registrarProducto/', views.registrarProducto),
    path('listaProductos/', views.lista, name='listaProductos'),
    path('ver-carrito/', views.carrito, name='ver_carrito'),
    path('agregar-al-carrito/<str:codigo>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<str:codigo>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    
    path('registrarCliente/', views.registrarCliente),
    path('cliente/', views.recl, name='cliente'),
    path('editarCliente/<codigo>', views.editarCliente,name='editarCliente'),
    path('edicionCliente/', views.edicionCliente),
    path('eliminarCliente/<codigo>', views.eliminarCliente, name='eliminarCliente'),

    path('Orfebreria',views.Orf,name='Orfebreria'),
    path('Esculturas',views.Esc,name='Esculturas'),
    path('Tejidos',views.Tej,name='Tejidos'),
    path('Otros',views.Otros,name='Otros'), 
     
     
    ]