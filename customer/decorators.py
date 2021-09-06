from django.shortcuts import render, redirect
from mobile.models import Cart,Orders

def loginrequired(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return func(request,*args,**kwargs)
    return wrapper

def permissionrequired(func):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("id")
        cart=Cart.objects.get(id=id)
        if request.user.username==cart.user:
            return func(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper

def orderpermission(func):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("id")
        order=Orders.objects.get(id=id)
        if request.user.username==order.user:
            return func(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper
