from django.urls import path,include
from .views import registration,login_view,sign_out,index,user_home,item_detail,add_to_cart,my_cart,del_cart,place_order,show_order,del_orderedlist


urlpatterns = [
    path("acount",registration,name="registration"),
    path("signin",login_view,name="login"),
    path("signout",sign_out,name="signout"),
    path("",index,name="index"),
    path("home",user_home,name="home"),
    path("item/<int:id>",item_detail,name="item_detail"),
    path("carts",my_cart,name="carts"),
    path("carts/<int:id>",add_to_cart,name="add_to_cart"),
    path("delcart/<int:id>",del_cart,name="delcart"),
    path("placeorder/<int:id>/<int:cid>",place_order,name="placeorder"),
    path("orderedlist",show_order,name="orderedlist"),
    path("delorder/<int:id>",del_orderedlist,name="delorder"),

]


