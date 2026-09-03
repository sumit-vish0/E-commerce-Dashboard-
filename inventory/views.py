from decimal import Decimal, InvalidOperation

from django.contrib import messages
from django.db.models import F, Sum, Count, DecimalField, ExpressionWrapper
from django.shortcuts import get_object_or_404, redirect, render

from .models import Product


def _product_form_data(request):
    name = request.POST.get("name", "").strip()
    category = request.POST.get("category", "").strip()
    supplier = request.POST.get("supplier", "").strip()

    if not name or not category or not supplier:
        raise ValueError("Required fields cannot be empty.")

    try:
        price = Decimal(request.POST.get("price", ""))
        quantity = int(request.POST.get("quantity", ""))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("Price must be a number and quantity must be an integer.")

    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative.")

    return name, category, price, quantity, supplier


def dashboard(request):
    products = Product.objects.all()[:10]
    total_products = Product.objects.count()
    total_quantity = Product.objects.aggregate(total=Sum("quantity"))["total"] or 0

    revenue_expr = ExpressionWrapper(
        F("price") * F("quantity"),
        output_field=DecimalField(max_digits=18, decimal_places=2),
    )
    revenue = Product.objects.aggregate(total=Sum(revenue_expr))["total"] or Decimal("0")

    return render(request, "inventory/dashboard.html", {
        "products": products,
        "total_products": total_products,
        "total_quantity": total_quantity,
        "revenue": revenue.quantize(Decimal("0.01")),
    })


def products(request):
    qs = Product.objects.all()

    search = request.GET.get("search", "").strip()
    category = request.GET.get("category", "").strip()
    min_price = request.GET.get("min_price", "").strip()
    max_price = request.GET.get("max_price", "").strip()
    stock = request.GET.get("stock", "").strip()

    if search:
        qs = qs.filter(name__icontains=search)
    if category:
        qs = qs.filter(category=category)
    if min_price:
        try:
            qs = qs.filter(price__gte=Decimal(min_price))
        except InvalidOperation:
            pass
    if max_price:
        try:
            qs = qs.filter(price__lte=Decimal(max_price))
        except InvalidOperation:
            pass
    if stock == "in":
        qs = qs.filter(quantity__gt=0)
    elif stock == "out":
        qs = qs.filter(quantity__lte=0)

    categories = Product.objects.values_list("category", flat=True).distinct().order_by("category")

    return render(request, "inventory/products.html", {
        "products": qs,
        "categories": categories,
        "filters": request.GET,
    })


def add_product(request):
    if request.method == "POST":
        try:
            name, category, price, quantity, supplier = _product_form_data(request)
        except ValueError as exc:
            messages.error(request, str(exc))
        else:
            Product.objects.create(
                name=name, category=category, price=price,
                quantity=quantity, supplier=supplier
            )
            messages.success(request, "Product added successfully.")
            return redirect("inventory:products")

    return render(request, "inventory/add_product.html", {"product": None})


def edit_product(request, pid):
    product = get_object_or_404(Product, pk=pid)

    if request.method == "POST":
        try:
            name, category, price, quantity, supplier = _product_form_data(request)
        except ValueError as exc:
            messages.error(request, str(exc))
        else:
            product.name = name
            product.category = category
            product.price = price
            product.quantity = quantity
            product.supplier = supplier
            product.save()
            messages.success(request, "Product updated successfully.")
            return redirect("inventory:products")

    return render(request, "inventory/add_product.html", {"product": product})


def delete_product(request, pid):
    product = get_object_or_404(Product, pk=pid)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect("inventory:products")


def revenue(request):
    products = Product.objects.all()
    total_revenue = sum((p.revenue for p in products), Decimal("0"))

    category_totals = {}
    for product in products:
        category_totals[product.category] = (
            category_totals.get(product.category, Decimal("0")) + product.revenue
        )

    category_revenue = []
    for category, amount in category_totals.items():
        percent = (amount / total_revenue * 100) if total_revenue else Decimal("0")
        category_revenue.append({
            "category": category,
            "revenue": amount.quantize(Decimal("0.01")),
            "percent": percent.quantize(Decimal("0.01")),
        })

    category_revenue.sort(key=lambda item: item["revenue"], reverse=True)

    return render(request, "inventory/revenue.html", {
        "products": products,
        "total_products": products.count(),
        "total_revenue": total_revenue.quantize(Decimal("0.01")),
        "category_revenue": category_revenue,
    })
