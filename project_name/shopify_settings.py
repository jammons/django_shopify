# Replace these empty values with values for you app. Fire up the runserver
# and read the docs for details on how to do this.

SHOPIFY_API_KEY = ''
SHOPIFY_API_SECRET = ''

# This file is in .gitignore so it won't be commited to the repository.
# To use it in production, you can use environ variables which will be
# checked here.
if SHOPIFY_API_KEY == '' and SHOPIFY_API_SECRET == '':
    import os
    SHOPIFY_API_KEY = os.environ.get('SHOPIFY_API_KEY', '')
    SHOPIFY_API_SECRET = os.environ.get('SHOPIFY_API_SECRET', '')

# Shopify uses the scopes parameter from OAuth2 to determine permissions
# See http://api.shopify.com/authentication.html for available scopes
SHOPIFY_API_SCOPE = ['read_products', 'read_orders']
