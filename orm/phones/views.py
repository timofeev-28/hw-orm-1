from django.shortcuts import get_object_or_404, render, redirect

from phones.models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    sort_by = request.GET.get("sort", "id")
    if sort_by == "min_price":
        sort_by = "price"
    elif sort_by == "max_price":
        sort_by = "-price"

    phones = Phone.objects.all().order_by(sort_by)
    template = "catalog.html"
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = "product.html"
    context = {"phone": phone}
    return render(request, template, context)
