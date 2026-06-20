from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Product
from .forms import ProductForm


@require_GET
def list_product(request):
    products = Product.objects.all().order_by("-id")
    return render(request, 'myapp/list_product.html', {"products": products})


@require_http_methods(["GET", "POST"])
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_product")
    else:
        form = ProductForm()
    return render(request, 'myapp/add_product.html', {"form": form})


@require_http_methods(["GET", "POST"])
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("list_product")
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/update_product.html', {"form": form, "product": product})


@require_POST
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("list_product")
