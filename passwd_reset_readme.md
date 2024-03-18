Use Django's password reset
In app/urls.py
```
from django.contrib.auth import views as auth_views

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_done.html'), name="password_reset_complete"),

```

Add SMTP config in settings
```
# SMTP configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'YOUR_EMAIL' 
EMAIL_HOST_PASSWORD = 'YOUR_PASSWORD' # There's some settings to be done, but it's not done in the tutorial
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
