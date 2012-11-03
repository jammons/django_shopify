from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf import settings
import shopify

from {{ project_name }}.shopify_app.forms import ShopLoginForm

def _return_address(request):
    return request.session.get('return_to') or reverse('home')

def login(request):
    # Ask user for their ${shop}.myshopify.com address

    # If the ${shop}.myshopify.com address is already provided in the URL,
    # just skip to authenticate
    if request.REQUEST.get('shop'):
        return authenticate(request)
    form = ShopLoginForm()
    #return render_to_response('shopify_app/login.html', { 'form': form }) 
    return render(request, 'shopify_app/login.html', { 'form': form, }) 

def authenticate(request):
    if request.method == 'POST':
        form = ShopLoginForm(request.POST)
        if form.is_valid():
            shop = form.cleaned_data['shop_name']
    if shop:
        scope = settings.SHOPIFY_API_SCOPE
        redirect_uri = 'http://%s%s' % (request.get_host(), reverse('shopify_finalize'))
        permission_url = shopify.Session.create_permission_url(shop.strip(), scope, redirect_uri)
        return redirect(permission_url)

    return redirect(_return_address(request))

def finalize(request):
    shop_url = request.REQUEST.get('shop')
    try:
        shopify_session = shopify.Session(shop_url, request.REQUEST)
    except shopify.ValidationException:
        messages.error(request, "Could not log in to Shopify store.")
        return redirect(reverse('shopify_login'))

    request.session['shopify'] = {
                "shop_url": shop_url,
                "access_token": shopify_session.token
            }
    messages.info(request, "Logged in to shopify store.")

    response = redirect(_return_address(request))
    request.session.pop('return_to', None)
    return response

def logout(request):
    request.session.pop('shopify', None)
    messages.info(request, "Successfully logged out.")

    return redirect(reverse('shopify_login'))
