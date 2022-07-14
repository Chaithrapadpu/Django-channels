from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/<int:id>', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path("register/", views.register_request, name="register"),
	path("login/", views.login_request, name="login"),
	path('removecart/<int:id>', views.removecart, name="removecart")

]