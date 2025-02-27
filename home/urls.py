from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
]







# Compare this snippet from portfolio/core/wsgi.py:
# """
# WSGI config for portfolioo project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see    https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/