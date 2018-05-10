from django.urls import path,include
from customer_portal.views import *
from django.conf.urls import url
urlpatterns = [
    url(r'^index/$',index),
    url(r'^login/$',login),
    url(r'^auth/$',auth_view),
    url(r'^logout/$',logout_view),
    url(r'^register/$',register),
    url(r'^registration/$',registration),
    url(r'^search/$',search),
    url(r'^search_results/$',search_results),
    url(r'^rent/$',rent_vehicle),
    url(r'^confirmed/',confirm),
    url(r'^manage/',manage),
    url(r'^update/',update_order),
    url(r'^delete/',delete_order),
]
