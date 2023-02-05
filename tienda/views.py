
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from tienda.Carrito import Carrito
from .models import *
from .forms import ContactoForm,CustomUserCreationForm
from django.contrib.auth import authenticate, login , logout
from rest_framework import viewsets
from .serializers import ProductoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def home(request):
    return render(request, 'tienda/home.html')

def donacion(request):
    return render(request, 'tienda/donacion.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'tienda/contacto.html', data)


def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"],password = formulario.cleaned_data["password1"])
            login(request, user)
            #messages.success(request, "Te has registrado correctamente")
            return redirect(to ="home")
            
        data["form"] = formulario

    return render(request, 'registration/registro.html' , data)


        
      

'''Desde aqui van las modificaciones del carrito XD'''
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")


@csrf_exempt
@api_view(['GET','PUT'])
def lista_producto(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_producto(request,id):
    try:
        producto = Producto.objects.get(producto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_404_NO_CONTENT)
        