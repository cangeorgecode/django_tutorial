This section references https://www.saaspegasus.com/guides/django-stripe-integrate/


Install necessary packages
```
pip install stripe dj-stripe
```

In settings.py,
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'djstripe',
]

# Stripe
STRIPE_TEST_PUBLIC_KEY = "CHANGE ME"
STRIPE_TEST_SECRET_KEY = "CHANGE ME"
STRIPE_LIVE_MODE = False
# Stripe dashboard > Developers > Webhooks > "endpoint_secret" on the right
DJSTRIPE_WEBHOOK_SECRET = "CHANGE ME"
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id" # Just needed to add this manually
```

Add the Stripe public key and the Stripe secret key in Django admin manually > api keys

To models.py, add 'MyStripeModel' 
```
python manage.py makemigrations
python manage.py migrate
python manage.py djstripe_sync_models price
```

In views.py, add
```
# Stripe subscription
from djstripe.models import Product

def index(request):
    return render(request, 'core/index.html', {'products': Product.objects.all()})
```

Add pricing table (Stripe > Product catalog > Pricing tables) to HTML template where you want it displayed

If you wish to view the djstripe model, run:
```
python3 manage.py shell
>>> from djstripe.models import Product
>>> products = Product.objects.all()
>>> product = Product.objects.get(id=1)
>>> print(product.__dict__) // This will show all the attributes
```












