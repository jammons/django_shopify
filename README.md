Django Shopify
=====================

This project should give you a good start towards developing a shopify app in Django. It's still under development. The goal is to have it provide a pinax bootstrap starter layer on top of Shopify's django implementation.

To Use:
--------

    $ mkdir [your_project_dir]
    $ cd !$
    $ django-admin.py startproject test_pro --template=https://github.com/jammons/django_shopify/zipball/master .


Setup:
--------

1. Create an account on [app.shopify.com](https://app.shopify.com/services/partners/auth/login)
1. Create an app and enter http://localhost:8000 for the application URL.
1. Open shopify_settings.py in your Django project directory.
1. Copy the API Key and Shared Key values as SHOPIFY_API_KEY and SHOPIFY_API_SECRET. If you know what permission scope you need you can edit that as well.
1. Run ./manage.py runserver
