from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


def homepage(request):
    categories = models.Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'homepage.html', context=context)


def show_products(request, pk):
    products = models.Products.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)


def show_product(request, pk):
    product = models.Products.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)


def add_product(request):
    form = forms.ProductsForms(request.POST, request.FILES)
    if form.is_valid():
        return redirect('show_products')
    context = {
        'form': form
    }
    return render(request, 'new.html', context=context)


def edit_product(request, pk):
    obj = get_object_or_404(models.Products, pk=pk)
    if request.method == 'POST':
        form = forms.ProductsForms(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_products')
    else:
        form = forms.ProductsForms(instance=obj)

    context = {
        'form': form
    }
    return render(request, 'edit.html', context=context)


def delete_product(request, pk):
    objecct = get_object_or_404(models.Products, pk=pk)
    if request.method == 'POST' or 'GET':
        objecct.delete()
        return render(request, 'delete.html')
