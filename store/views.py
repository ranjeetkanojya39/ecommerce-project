from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q


# 🛒 STORE VIEW
def store(request, category_slug=None):
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True).order_by('id')

    paginator = Paginator(products, 3)  # change per page here
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'product_count': products.paginator.count,
    }

    return render(request, 'store/store.html', context)


# 📦 PRODUCT DETAIL
def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(
        Product,
        category__slug=category_slug,
        slug=product_slug
    )

    if request.user.is_authenticated:
        in_cart = CartItem.objects.filter(
            user=request.user,
            product=single_product
        ).exists()
    else:
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request),
            product=single_product
        ).exists()

    context = {
        'single_product': single_product,
        'in_cart': in_cart
    }

    return render(request, 'store/product_detail.html', context)


# 🔍 SEARCH
def search(request):
    products = Product.objects.none()

    keyword = request.GET.get('keyword')

    if keyword:
        products = Product.objects.filter(
            Q(description__icontains=keyword) |
            Q(product_name__icontains=keyword)
        ).order_by('-created_date')

    context = {
        'products': products,
        'product_count': products.count()
    }

    return render(request, 'store/store.html', context)