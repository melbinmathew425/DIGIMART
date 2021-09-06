
from django.urls import path
from mobile.views import add_brand,llist_brand,update_brand,delete_brand,product_create,list_products,edit_item,detail_product,delete_product

urlpatterns = [
    path("brands",add_brand,name="brands"),
    path("listbrands",llist_brand,name="listbrands"),
    path("updatebrand/<int:id>",update_brand,name="updatebrand"),
    path("deletebrand/<int:id>",delete_brand,name="deletebrand"),
    path("products",product_create,name="products"),
    path("items",list_products,name="product_list"),
    path("change/<int:id>",edit_item,name="change"),
    path("details/<int:id>",detail_product,name="details"),
    path("remove/<int:id>",delete_product,name="remove")
]
