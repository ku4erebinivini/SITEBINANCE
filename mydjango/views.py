from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.shortcuts import render
from .binance import get_ethereum_price, get_tron_price, get_bitcoin_price


def index(request):
    return render(request, 'mydjango/index.html')


def index(request):
    ethereum_price = get_ethereum_price()
    bitcoin_price = get_bitcoin_price()
    tron_price = get_tron_price()
    return render(request, 'mydjango/index.html', {'ethereum_price': ethereum_price, 'bitcoin_price': bitcoin_price, 'tron_price': tron_price})


