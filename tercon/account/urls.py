from django.urls import re_path
from .views import account, cancel_subscription, reactivate_subscription

urlpatterns = [
    re_path(r'^$', account, name='account'),
    re_path(r'^cancel/(?P<subscription_id>[0-9A-Za-z_]+)$', cancel_subscription, name='cancel_subscription'),
    re_path(r'^reactivate/(?P<subscription_id>[0-9A-Za-z_]+)$', reactivate_subscription, name='reactivate_subscription')]