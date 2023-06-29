from django.shortcuts import render,redirect
from .models import  Cliente , Artista ,Producto

# Create your views here.
def home(request):
    return render(request, 'principal.html')

def Orf(request):
    return render(request,'Orfebreria.html')
def Esc(request):
    return render(request,'Esculturas.html') 
def Tej(request):
    return render(request,'Tejidos.html')

def Otros(request):
    Productos = Producto.objects.all()
    return render(request,'Otros.html',{'productos':Productos})

def val(request):
    return render(request, 'validacion.html' )

def art(request):
    return render(request, 'artistas.html')

def col(request):
    return render(request, 'coloresDios.html')

def crea(request):
    return render(request, 'creacionAdan.html')

def elg(request):
    return render(request, 'ElGrito.html')

def jap(request):
    return render(request, 'japo.html')

def pint(request):
    return render(request, 'pinturas.html')

def sobr(request):
    return render(request, 'sobre_nosotros.html')

def cur(request):
    Clientes = Cliente.objects.all()
    return render(request, 'gestionCurso.html', {"Clientes": Clientes})



def adpro(request):
    return render(request, 'adproducto.html')


def registrarProducto(request):
    codigo      = request.POST['txtCodigo']
    nombre      = request.POST['txtNombre']
    precio      = request.POST['numPrecio']
    stock       = request.POST['numStock']
    imagen      = request.POST['txtImagen']
    
    producto= Producto.objects.create(
        codigo= codigo, nombre= nombre,precio= precio, stock= stock, imagen= imagen)
    return redirect('/listaProductos')

def agregar_al_carrito(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    
    # Obtén el carrito de la cookie del usuario
    carrito = request.COOKIES.get('carrito', '')
    
    # Agrega el código del producto al carrito
    carrito += codigo + ","
    
    # Establece la cookie con el carrito actualizado
    response = redirect('Otros')
    response.set_cookie('carrito', carrito)
    
    return response


def eliminar_del_carrito(request, codigo):
    # Obtén el carrito de la cookie del usuario
    carrito = request.COOKIES.get('carrito', '')
    
    # Elimina el código del producto del carrito
    carrito = carrito.replace(codigo + ",", "")
    
    # Establece la cookie con el carrito actualizado
    response = redirect('ver_carrito')
    response.set_cookie('carrito', carrito)
    
    return response



def carrito(request):
    carrito = request.COOKIES.get('carrito', '').split(",")
    
    # Filtra los códigos de producto no vacíos
    codigos_productos = [codigo for codigo in carrito if codigo]
    
    # Obtén los productos correspondientes a los códigos filtrados
    productos = Producto.objects.filter(codigo__in=codigos_productos)
    
    return render(request, 'ver_carrito.html', {'productos': productos})





def lista(request):
    Productos = Producto.objects.all()
    return render(request,'lista_productos.html',{'productos':Productos})

def rear(request):
    return render(request, 'RegistroArtista.html')

def recl(request):
    return render(request, 'registro_cliente.html')


def registrarCliente(request):
    codigo      = request.POST['txtCodigo']
    nombre      = request.POST['txtNombre']
    apellidos   = request.POST['txtApellidos']
    correo      = request.POST['txtCorreo']
    celular     = request.POST['numCelular']
    edad        = request.POST['numEdad']
    contrasena  = request.POST['txtContraseña']
    
    cliente= Cliente.objects.create(
        codigo= codigo, nombre= nombre, apellidos=apellidos, correo=correo, celular=celular, edad=edad, contrasena=contrasena)
    return redirect('/')

def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect('/curso')

def editarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    return render(request, 'editarCliente.html', {"cliente" : cliente})

def edicionCliente(request):
    codigo      = request.POST['txtCodigo']
    nombre      = request.POST['txtNombre']
    apellidos   = request.POST['txtApellidos']
    correo      = request.POST['txtCorreo']
    celular     = request.POST['numCelular']
    edad        = request.POST['numEdad']
    contrasena  = request.POST['txtContraseña']
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.nombre = nombre
    cliente.apellidos = apellidos
    cliente.correo = correo
    cliente.celular = celular
    cliente.edad = edad
    cliente.contrasena = contrasena
    cliente.save()
    return redirect('/curso')
#artista 

def registrarArtista(request):
    codigo      = request.POST['txtCodigo']
    nombre      = request.POST['txtNombre']
    apellidos   = request.POST['txtApellidos']
    correo      = request.POST['txtCorreo']
    celular     = request.POST['numCelular']
    arte        = request.POST['numArte']
    argumento  = request.POST['txtArgumento']
    
    artista= Artista.objects.create(
        codigo= codigo, nombre= nombre, apellidos=apellidos, correo=correo, celular=celular, arte=arte, argumento=argumento)
    return redirect('/')

def eliminarArtista(request, codigo):
    artista = Artista.objects.get(codigo=codigo)
    artista.delete()
    return redirect('/')

def editarArtista(request, codigo):
    artista = Artista.objects.get(codigo=codigo)
    return render(request, 'editarArtista.html', {"artista" : artista})

def edicionArtista(request):
    codigo      = request.POST['txtCodigo']
    nombre      = request.POST['txtNombre']
    apellidos   = request.POST['txtApellidos']
    correo      = request.POST['txtCorreo']
    celular     = request.POST['numCelular']
    arte        = request.POST['numArte']
    argumento  =  request.POST['txtArgumento']
    artista = Cliente.objects.get(codigo=codigo)
    artista.nombre = nombre
    artista.apellidos = apellidos
    artista.correo = correo
    artista.celular = celular
    artista.arte = arte
    artista.argumento = argumento
    artista.save()
    return redirect('/')