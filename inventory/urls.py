from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("products/", views.products, name="products"),
    path("add-product/", views.add_product, name="add_product"),
    path("edit/<int:pid>/", views.edit_product, name="edit_product"),
    path("delete/<int:pid>/", views.delete_product, name="delete_product"),
    path("revenue/", views.revenue, name="revenue"),
]
