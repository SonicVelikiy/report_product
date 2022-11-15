from django.urls import path
from .views import home, add_product
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', home, name='home'),
    path('addproduct/', add_product, name='addproduct'),
    path('accounts/login/', auth_views.LoginView.as_view()),
]
