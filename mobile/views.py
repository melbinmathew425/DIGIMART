from django.shortcuts import render, redirect
from mobile.forms import BrandModelForm, ProductCreationForm
from mobile.models import Brand, Product


def add_brand(request):
    form = BrandModelForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BrandModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "addbrand.html", context)
    return render(request,"addbrand.html",context)


def llist_brand(request):
    brands = Brand.objects.all()
    context = {}
    context["brands"] = brands
    return render(request, "listbrand.html", context)


def update_brand(request, id):
    brand = Brand.objects.get(id=id)
    form = BrandModelForm(instance=brand)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BrandModelForm(instance=brand, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrands")
    return render(request, "editbrand.html", context)


def delete_brand(request, id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    return redirect("listbrands")


def product_create(request):
    form = ProductCreationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductCreationForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else :
            context["form"]=form
            return render(request, "product.html", context)
    return render(request, "product.html", context)


def list_products(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "listmobile.html", context)

def get_object(id):
    return Product.objects.get(id=id)

def edit_item(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    form=ProductCreationForm(instance=product)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreationForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    return render(request,"edit_product.html",context)

def detail_product(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    context={}
    context["product"]=product
    return render(request,"detail_product.html",context)
def delete_product(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    product.delete()
    return redirect("product_list")