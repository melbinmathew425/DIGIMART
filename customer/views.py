from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,LoginForm,PlaceOrderForm
from django.contrib.auth import authenticate,login,logout
from mobile.models import Product,Cart,Orders
from mobile.views import get_object as get_product
from .decorators import loginrequired,permissionrequired,orderpermission
from django.db.models import Sum
# Create your views here.

def get_cart_count(user):
    count=Cart.objects.filter(user=user,status='ordernotplaced').count()
    return count
def registration (request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"]=form
    return render(request,"registration.html",context)

def login_view(request,*args,**kwargs):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return redirect("home")
            else:
                print("failed")
                context["form"]=form
    return render(request,"login.html",context)

def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("login")
def index(request):
    return render(request,"index.html")


def user_home(request,*args,**kwargs):
    mobiles=Product.objects.all()
    count=get_cart_count(request.user)
    print(count)
    context={
        "count":count,
        "mobiles":mobiles
    }
    return render(request,"home.html",context)


@loginrequired
def item_detail(request,*args,**kwargs):
    id=kwargs.get("id")
    mobile=Product.objects.get(id=id)
    context={"mobile":mobile}
    return render(request,"productdetail.html",context)

@loginrequired
def add_to_cart(request,*args,**kwargs):
    pid=kwargs.get("id")
    product=get_product(pid)
    cart=Cart(product=product,user=request.user)
    cart.save()
    return redirect("home")

@loginrequired
def my_cart(request,*args,**kwargs):
    cart_item=Cart.objects.filter(user=request.user,status="ordernotplaced")
    total = Cart.objects.filter(status='ordernotplaced', user=request.user).aggregate(Sum('product__price'))
    context={
        "cart_items":cart_item,
        "total":total.get("product__price__sum")
    }
    return render(request,"addtocart.html",context)

@loginrequired
@permissionrequired
def del_cart(request,*args,**kwargs):
    id=kwargs.get("id")
    cart=Cart.objects.get(id=id)
    cart.delete()
    return redirect("carts")

@loginrequired
def place_order(request,*args,**kwargs):
    pid=kwargs.get("id")
    mobile=get_product(pid)
    count=get_cart_count(request.user)
    context={
        "form":PlaceOrderForm(initial={"product":mobile.mobile_name}),
        "count":count
    }
    if request.method == "POST":
        print(kwargs)
        cid=kwargs.get("cid")
        cart=Cart.objects.get(id=cid)
        form=PlaceOrderForm(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            product=mobile
            order=Orders(address=address,product=product,user=request.user)
            order.save()
            cart.status="orderplaced"
            cart.save()
            return redirect("carts")
    return render(request,"placeorder.html",context)

@loginrequired
def show_order(request,*args,**kwargs):
    ordered_items=Orders.objects.filter(user=request.user)
    context={}
    context["ordered_items"]=ordered_items
    count=get_cart_count(request.user)
    context["count"]=count
    return render(request,"orderedlist.html",context)

@loginrequired
@orderpermission

def del_orderedlist(request,*args,**kwargs):
    id=kwargs.get("id")
    order=Orders.objects.get(id=id)
    print(order)
    order.status="cancelled"
    order.save()
    # order.delete()
    return redirect("home")
