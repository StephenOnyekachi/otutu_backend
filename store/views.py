import random
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from .models import *
from store.models import Items

# Create your views here.


def index(request):
    return render(request, 'index.html')

def store(request):
    user = request.user
    items = Items.objects.filter(is_avaliable=True).order_by('-id')
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        cart = Cart.objects.filter(user=profile, paid=False, suplid=False)
        context = {
            'items':items,
            "cart":cart,
        }
    context = {
        'items':items,
    }
    return render(request, 'store.html', context)

def tocart(request, pk):
    user = request.user
    item = Items.objects.get(id=pk)
    if request.method == "POST":
        item = request.POST.get('item')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        total = int(price) * int(quantity)
        Cart.objects.create(
            item_id=item,
            quantity= quantity,
            total=total,
            user=profile
        )
        return redirect('store')
    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        cart = Cart.objects.filter(user=profile, paid=False, suplid=False)
        context = {
            'item':item,
            "user":profile,
            "cart":cart,
        }
    context = {
        "item":item,
    }
    return render(request, 'tocart.html', context)

@login_required(login_url='login')
def cart(request):
    total = 0
    user = request.user
    profile = Profile.objects.get(user=user)
    cart = Cart.objects.filter(user=profile, paid=False, suplid=False)
    if cart:
        for cart_price in cart:
            total_price = cart_price.total
            total_len = len(cart)
        total += total_price * total_len
    context = {
        "cart":cart,
        "total":total,
    }
    return render(request, 'cart.html', context)

def remove_cart(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    messages.info(request, "you remove an item from cart")
    return redirect('cart')

@login_required(login_url='login')
def newitem(request):
    if request.method == "POST":
        text = request.POST.get('name')
        out_number = request.POST.get('number')
        selling_price = request.POST.get('sprice')
        but_price = request.POST.get('bprice')
        image = request.FILES.get('image')
        des = request.POST.get('des')
        quantity = request.POST.get('quantity')
        name = text.lower()
        Items.objects.create(
            name = name,
            out_number = out_number,
            selling_price = selling_price,
            but_price = but_price,
            image = image,
            des = des,
            quantity = quantity,
        )
        return redirect('dashboad')
    return render(request, 'newitem.html')

@login_required(login_url='login')
def viewitem(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == "POST":
        selling_price = request.POST.get('sprice')
        but_price = request.POST.get('bprice')
        quantity = request.POST.get('quantity')

        item.selling_price = selling_price
        item.but_price = but_price
        item.quantity = quantity
        item.save()
        return redirect('dashboad')
    context = {
        'item':item,
    }
    return render(request, 'viewitem.html', context)

def deleteitem(request, pk):
    item = Items.objects.get(id=pk)
    item.delete()
    return redirect('dashboad')

def is_avaliable(request, pk):
    item = Items.objects.get(id=pk)
    if item.is_avaliable:
        item.is_avaliable = False
        item.save()
    else:
        item.is_avaliable = True
        item.save()
    return redirect('dashboad')

@login_required(login_url='login')
def dashboad(request):
    items = Items.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'dashboad.html', context)

@login_required(login_url='login')
def pricelist(request):
    items = Items.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'pricelist.html', context)

@login_required(login_url='login')
def sells(request):
    item = Items.objects.all()
    sells = SellsNote.objects.all().order_by('-id')
    if request.method == "POST":
        product = request.POST.get('item')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        total = int(price) * int(quantity)

        sold = Items.objects.get(id=product)
        sold.quantity -= int(quantity)
        sold.save()

        SellsNote.objects.create(
            item_id=product,
            quantity=quantity,
            price=price,
            total=total,
        )
        messages.success(request, "new sells report created")
        return redirect('sells')
    context = {
        "item":item,
        "sells":sells,
    }
    return render(request, 'sells.html', context)

@login_required(login_url='login')
def credite(request):
    credite = CrediteNote.objects.all().order_by('-id')
    if request.method == "POST":
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        note = request.POST.get("note")
        CrediteNote.objects.create(
            price=price,
            quantity=quantity,
            name=name,
            number=phone,
            note=note
        )
        messages.success(request, "you just make new credite note")
        return redirect('credite')
    context = {
        "credite":credite,
    }
    return render(request, 'credite.html', context)

def paid(request, pk):
    item = CrediteNote.objects.get(id=pk)
    item.paid = True
    item.save()
    messages.success(request, "item was made paid")
    return redirect('credite')

@login_required(login_url='login')
def order(request):
    cart = Cart.objects.all()
    context = {
        "cart":cart,
    }
    return render(request, 'order.html', context)

def is_paid(request, pk):
    item = Cart.objects.get(id=pk)
    item.paid = True
    item.save()
    messages.success(request, "item was made paid")
    return redirect('order')

def is_suplied(request, pk):
    item = Cart.objects.get(id=pk)
    item.suplid = True
    item.save()
    messages.success(request, "item was suplied")
    return redirect('order')

def search(request):
    if request.method == "GET":
        text = request.GET.get('item')
        search = text.lower()
        multiple = Q(Q(out_number=search)|Q(name=search)|Q(des=search))
        items = Items.objects.filter(multiple)
    context = {
        "items":items,
        "search":search,
    }
    return render(request, 'search.html', context)

def search2(request):
    if request.method == "GET":
        text = request.GET.get('item')
        search = text.lower()
        multiple = Q(Q(name=search)|Q(des=search))
        items = Items.objects.filter(multiple)
    context = {
        "items":items,
        "search":search,
    }
    return render(request, 'search2.html', context)


