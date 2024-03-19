from django.db import models

# This is for Stripe subscription
class MyStripeModel(models.Model):
    name = models.CharField(max_length=100)
    stripe_subscription_id = models.CharField(max_length=100)
