from urllib.parse import urlparse, urlunparse

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import QueryDict, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.contrib.auth.decorators import login_required
from .models import product
from django.shortcuts import redirect
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "home.html")


def add_product(request):
    return render(request, 'add_product.html')
