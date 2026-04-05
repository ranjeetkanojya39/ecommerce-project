from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# 🔑 Session Cart ID
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# 🎯 Get Product Variations
def get_product_variation(request, product):
    product_variation = []
    if request.method == 'POST':
        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(
                    product=product,
                    variation_category__iexact=key,
                    variation_value__iexact=value
                )
                product_variation.append(variation)
            except Variation.DoesNotExist:
                continue
    return product_variation


# ➕ ADD TO CART
def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_variation = get_product_variation(request, product)

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(product=product, user=request.user)

        if cart_items.exists():
            ex_var_list = []
            item_ids = []

            for item in cart_items:
                existing_variation = list(item.variations.all())
                ex_var_list.append(sorted(existing_variation, key=lambda x: x.id))
                item_ids.append(item.id)

            sorted_variation = sorted(product_variation, key=lambda x: x.id)

            if sorted_variation in ex_var_list:
                index = ex_var_list.index(sorted_variation)
                item = CartItem.objects.get(id=item_ids[index])
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    user=request.user
                )
                if product_variation:
                    item.variations.add(*product_variation)
        else:
            item = CartItem.objects.create(
                product=product,
                quantity=1,
                user=request.user
            )
            if product_variation:
                item.variations.add(*product_variation)

    else:
        cart, _ = Cart.objects.get_or_create(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(product=product, cart=cart)

        if cart_items.exists():
            ex_var_list = []
            item_ids = []

            for item in cart_items:
                existing_variation = list(item.variations.all())
                ex_var_list.append(sorted(existing_variation, key=lambda x: x.id))
                item_ids.append(item.id)

            sorted_variation = sorted(product_variation, key=lambda x: x.id)

            if sorted_variation in ex_var_list:
                index = ex_var_list.index(sorted_variation)
                item = CartItem.objects.get(id=item_ids[index])
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    cart=cart
                )
                if product_variation:
                    item.variations.add(*product_variation)
        else:
            item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )
            if product_variation:
                item.variations.add(*product_variation)

    return redirect('cart')


# ➖ REMOVE SINGLE ITEM QUANTITY
def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(
                product=product,
                user=request.user,
                id=cart_item_id
            )
        else:
            cart, _ = Cart.objects.get_or_create(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(
                product=product,
                cart=cart,
                id=cart_item_id
            )

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    except CartItem.DoesNotExist:
        pass

    return redirect('cart')


# ❌ REMOVE COMPLETE ITEM
def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)

    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(
                product=product,
                user=request.user,
                id=cart_item_id
            )
        else:
            cart, _ = Cart.objects.get_or_create(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(
                product=product,
                cart=cart,
                id=cart_item_id
            )

        cart_item.delete()

    except CartItem.DoesNotExist:
        pass

    return redirect('cart')


# 🧾 CART VIEW
def cart(request):
    total = 0
    quantity = 0
    cart_items = []
    tax = 0
    grand_total = 0

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart, _ = Cart.objects.get_or_create(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for item in cart_items:
            total += item.product.price * item.quantity
            quantity += item.quantity

        tax = (2 * total) / 100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)


# 💳 CHECKOUT
def checkout(request):
    return render(request, 'store/checkout.html')