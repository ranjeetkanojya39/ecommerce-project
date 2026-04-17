from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # 1. Cart fetch karein session id se
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            
            # 2. LOGIC BUG FIX: Check karein agar user login hai
            if request.user.is_authenticated:
                # Login user ke saare cart items lo (Database user field se)
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                # Guest user ke liye session cart se items lo
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            
            # 3. Loop karke total quantity calculate karein
            for  cart_item in cart_items:
                cart_count += cart_item.quantity
                
        except Cart.DoesNotExist:
            cart_count = 0
            
    return dict(cart_count=cart_count)