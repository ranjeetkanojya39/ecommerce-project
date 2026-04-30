from django.shortcuts import render, redirect
from cart.views import _cart_id 
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Email verification imports

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

#from carts.views import _cart_id

from cart.models import  Cart, CartItem
import requests


# ================= REGISTER =================
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Form se data nikalna
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Username email se generate
            username = email.split("@")[0]

            # User create karna
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            user.phone_number = phone_number
            user.is_active = True   # ❗ IMPORTANT (email verify hone tak inactive)
            user.save()

            # ===== Email Verification =====
            current_site = get_current_site(request)

            mail_subject = 'Please activate your account'

            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site.domain,  # ✔ fix
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_email = EmailMessage(mail_subject, message, to=[email])
            send_email.send()

            # Success message + redirect
            messages.success(
                request,
                'Registration successful! Please check your email to activate your account.'
            )

            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


# ================= LOGIN =================
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                print('entering inside try block')
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                print(is_cart_item_exists)
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    print(cart_item)

                    for item in cart_item:
                        item.user = user
                        item.save()
            except:
                print('entering inside except block')
                pass
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


# ================= DASHBOARD =================
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


# ================= LOGOUT =================
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')


# ================= ACTIVATE ACCOUNT =================
def activate(request, uidb64, token):
    try:
        # UID decode karna
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    # Token check
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Your account is activated successfully!')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


# ================= FORGOT PASSWORD =================
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email=email)

            # Send reset email
            current_site = get_current_site(request)

            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_email = EmailMessage('Reset Your Password', message, to=[email])
            send_email.send()

            messages.success(request, 'Password reset email sent!')
            return redirect('login')

        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')

    return render(request, 'accounts/forgotPassword.html')


# ================= RESET PASSWORD VALIDATION =================
def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Session me uid store
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has expired!')
        return redirect('login')


# ================= RESET PASSWORD =================
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)

            user.set_password(password)  # secure hashing
            user.save()

            messages.success(request, 'Password reset successful!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('resetPassword')

    return render(request, 'accounts/resetPassword.html')



@login_required(login_url='login')
def my_orders(request):
    return render(request, 'accounts/my_orders.html')